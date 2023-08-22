---
title: Docker
description: Fundamentos de docker III
author: Claudio Andres Salamanca
tags: Docker, Introduccion
date_published: 2023-08-01
---


# Mejores prácticas para los Dockerfiles


# Ejemplo práctico

Aquí hay un pequeño Dockerfile, con varios errores posibles. A continuación, lo intentaremos arreglar! Supongamos que queremos crear la aplicación web de node.js. Aquí está (CMD es complicado y probablemente no funcione, pero es solo un ejemplo):

```bash
FROM ubuntu

ADD . /app

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y nodejs ssh mysql
RUN cd /app && npm install

# this should start three processes, mysql and ssh
# in the background and node app in foreground
# isn't it beautifully terrible? <3
CMD mysql & sshd & npm start
```
Para construir usamos: ``` $ docker build -t wtf . ```

¿Puedes ver todos los errores aquí? Intentaremos arreglarlos

# 1. Añadir un .dockerignore

Al construir la imagen, Docker prepara primero el  __context__  recopilando todos los archivos que se pueden usar en un proceso. El contexto predeterminado contiene todos los archivos en un directorio Dockerfile. Por lo general, ___no queremos incluir bibliotecas descargadas en el directorio___ .git y archivos compilados. El archivo .dockerignore se ve exactamente como .gitignore, por ejemplo:

```
.git/
node_modules/
dist/
```

# 2. El docker debe 'hacer una cosa'.

Técnicamente puede iniciar varios procesos dentro del contenedor de Docker. `PUEDE` poner las aplicaciones de base de datos, frontend y backend, ssh, supervisor en una imagen de docker. __"Puedes pero no debes"__:

- Largos tiempos de construcción (el cambio en, por ejemplo, el frontend obligará a todo el backend a reconstruirse)
- Imágenes muy grandes y pesadas
- Registro difícil desde muchas aplicaciones (
- Desperdicio en un escalado  horizontal
- Problemas con los procesos zombies: debes recordar el proceso de inicio adecuado.

Mi consejo es preparar una imagen de Docker separada para cada componente, y usar [Docker Compose](https://docs.docker.com/compose/) para iniciar fácilmente múltiples contenedores al mismo tiempo.

Vamos a eliminar los paquetes innecesarios de nuestro Dockerfile. SSH puede ser reemplazado con [docker exec](https://docs.docker.com/engine/reference/commandline/exec/)

```
FROM ubuntu

ADD . /app

RUN apt-get update
RUN apt-get upgrade -y

# we should remove ssh and mysql, and use
# separate container for database 
RUN apt-get install -y nodejs  # ssh mysql
RUN cd /app && npm install

CMD npm start
```

# 3. Combinar múltiples comandos RUN en uno

Docker funciona creando muchas capas. El conocimiento de cómo funcionan es esencial.

- Cada comando en Dockerfile crea la llamada __capa__
- Las capas se almacenan en caché y se reutilizan.
- Invalidar el caché de una sola capa invalida todas las capas subsiguientes
- La invalidación se produce después del cambio de comando, si los archivos copiados son diferentes, o la variable de compilación es diferente a la anterior
- Las capas son inmutables, por lo que si agregamos un archivo en una capa y lo eliminamos en la siguiente, la imagen STILL contiene ese archivo (simplemente no está disponible en el contenedor).


Optimicemos nuestro ejemplo. Estamos fusionando todos los comandos RUN en uno, y eliminando apt-get upgrade,ya que hace que nuestra compilación no sea determinista (confiamos en nuestras actualizaciones de imagen base):

```
FROM ubuntu

ADD . /app

RUN apt-get update \
    && apt-get install -y nodejs \
    && cd /app \
    && npm install

CMD npm start
```
Tenga en cuenta que debe combinar comandos con una probabilidad similar de cambio. Actualmente, cada vez que cambia nuestro código fuente, necesitamos reinstalar todos los nodejs. Entonces, una mejor opción es:

```
FROM ubuntu

RUN apt-get update && apt-get install -y nodejs 
ADD . /app
RUN cd /app && npm install

CMD npm start
```

# 4. No use la etiqueta de imagen base 'latest'

La  etiqueta __latest__ esta por defecto, se utiliza cuando no se especifica ninguna otra etiqueta. Entonces nuestra instrucción en el Dockerfile __"FROM ubuntu:latest"__ realidad hace exactamente lo mismo que "La imagen de  ubuntu: más reciente". Pero la etiqueta 'latest' apuntará a una imagen diferente cuando se lance una nueva versión, y su compilación podría dar problemas. Por lo tanto, a menos que esté creando un Dockerfile genérico que debe estar actualizado con la imagen base, proporcione una etiqueta específica.

En nuestro ejemplo, usemos la etiqueta 16.04:

```
FROM ubuntu:16.04  # it's that easy!

RUN apt-get update && apt-get install -y nodejs 
ADD . /app
RUN cd /app && npm install

CMD npm start
```

# 5. Elimine los archivos innecesarios después de cada paso de RUN

Para empezar actualizamos las fuentes de apt-get, instalamos unos pocos paquetes, solo los necesarios para compilar, descargamos y extrajimos archivos. Obviamente no los necesitamos en nuestras imágenes finales, así que mejor hagamos una limpieza. `¡El tamaño es importante!`

En nuestro ejemplo podemos eliminar las listas de apt-get (creadas por apt-get update):
```
FROM ubuntu:16.04

RUN apt-get update \
    && apt-get install -y nodejs \
    # added lines
    && rm -rf /var/lib/apt/lists/*

ADD . /app
RUN cd /app && npm install

CMD npm start
```

# 6. Usa la imagen base adecuada

En nuestro ejemplo, usamos ubuntu. ¿Pero por qué? ¿Realmente necesitamos una imagen base de propósito general, cuando solo queremos ejecutar la aplicación de node? Una mejor opción es usar una imagen especializada con el node ya instalado:

```
FROM node

ADD . /app
# we don't need to install node 
# anymore and use apt-get
RUN cd /app && npm install

CMD npm start
```
O incluso mejor, podemos elegir la versión __Alpine__ (alpine es una distribución de linux muy pequeña, con un tamaño de aproximadamente 4 MB. Esto lo convierte en el candidato perfecto para una imagen base)

```
FROM node:7-alpine

ADD . /app
RUN cd /app && npm install

CMD npm start
```
Alpine tiene gestor de paquetes, llamado apk. Es un poco diferente de apt-get, pero aún así es bastante fácil de aprender. Además, tiene algunas características realmente útiles, como las opciones --o-cache y --virtual. De esa manera, elegimos lo que queremos exactamente a nuestra imagen, nada más.

# 7. Configurar WORKDIR and CMD

El comando WORKDIR cambia el directorio predeterminado, donde ejecutamos nuestros comandos RUN / CMD / ENTRYPOINT.

CMD es un comando predeterminado que se ejecuta después de crear un contenedor sin otro comando especificado. Suele ser la acción más frecuente. Vamos a agregarlos a nuestro Dockerfile

```
FROM node:7-alpine

WORKDIR /app
ADD . /app
RUN npm install

CMD ["npm", "start"]
```
Debe poner su comando entre paréntesis, una palabra por elemento [más en la documentación oficial](https://docs.docker.com/engine/reference/builder/#cmd)

# 8. Usa ENTRYPOINT (opcional)

No siempre es necesario porque el ENTRYPOINT agrega complejidad. ¿Como funciona?

Entrypoint es una secuencia de comandos, que se ejecutará en lugar de comando, y recibirá el comando como argumentos. Es una excelente manera de crear imágenes ejecutables de Docker:

```
#!/usr/bin/env sh
# $0 is a script name, 
# $1, $2, $3 etc are passed arguments
# $1 is our command
CMD=$1

case "$CMD" in
  "dev" )
    npm install
    export NODE_ENV=development
    exec npm run dev
    ;;

  "start" )
    # we can modify files here, using ENV variables passed in 
    # "docker create" command. It can't be done during build process.
    echo "db: $DATABASE_ADDRESS" >> /app/config.yml
    export NODE_ENV=production
    exec npm start
    ;;

   * )
    # Run custom command. Thanks to this line we can still use 
    # "docker run our_image /bin/bash" and it will work
    exec $CMD ${@:2}
    ;;
esac
```
Guárdelo en su directorio raíz, llamado entrypoint.sh. Usalo en Dockerfile:

```
FROM node:7-alpine

WORKDIR /app
ADD . /app
RUN npm install

ENTRYPOINT ["./entrypoint.sh"]
CMD ["start"]
```
Ahora podemos ejecutar esta imagen de forma ejecutable:
docker run our-app dev
docker run our-app start
docker run -it our-app /bin/bash - - este también funcionará

# 9. Utilice "exec" dentro script entrypoint

Como puedes ver en el ejemplo entrypoint, estamos usando __exec__ . Sin él, no podríamos detener nuestra aplicación correctamente. Exec básicamente reemplaza el proceso de script por uno nuevo, por lo que todas las señales y códigos de salida funcionan según lo previsto.

# 10. Mejor COPY que usar ADD

COPY es más simple. ADD tiene cierta lógica para descargar archivos remotos y extraer archivos, [más en la documentación oficial](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/#add-or-copy). Sólo quédate con COPY.

ADD puede ser útil si su compilación depende de recursos externos, y usted quiere la invalidación de la caché de compilación adecuada. No es la mejor práctica, pero a veces es la única manera.

Añadimos ... ADD, copia esto a nuestro ejemplo:
```
FROM node:7-alpine

WORKDIR /app

COPY . /app
RUN npm install

ENTRYPOINT ["./entrypoint.sh"]
CMD ["start"]
```
# 11. Optimizamos COPY y RUN
Deberíamos poner los cambios menos frecuentes en la parte superior de nuestros Dockerfiles para aprovechar el almacenamiento en caché.

En nuestro ejemplo, el código cambiará a menudo y no queremos volver a instalar los paquetes cada vez. Podemos copiar ___package.json___ antes del resto del código, instalar dependencias y luego agregar otros archivos. Apliquemos esa mejora a nuestro Dockerfile:
```
FROM node:7-alpine

WORKDIR /app

COPY package.json /app
RUN npm install
COPY . /app

ENTRYPOINT ["./entrypoint.sh"]
CMD ["start"]
```
# 12. Indicar en las variables de entorno  puertos and volumenes

Necesitamos algunas variables de entorno para ejecutar nuestro contenedor. Es una buena práctica establecer valores predeterminados en Dockerfile. Además, debemos exponer todos los puertos utilizados y definir volúmenes. 

Próxima mejora a nuestro ejemplo:
```
FROM node:7-alpine

# env variables required during build
ENV PROJECT_DIR=/app

WORKDIR $PROJECT_DIR

COPY package.json $PROJECT_DIR
RUN npm install
COPY . $PROJECT_DIR

# env variables that can change
# volume and port settings
# and defaults for our application
ENV MEDIA_DIR=/media \
    NODE_ENV=production \
    APP_PORT=3000

VOLUME $MEDIA_DIR
EXPOSE $APP_PORT

ENTRYPOINT ["./entrypoint.sh"]
CMD ["start"]
```
Estas variables estarán disponibles en el contenedor. Si necesita variables de solo compilación, use args de compilación en su lugar.

# 13. Añadir metadatos a la imagen usando LABEL.

Hay una opción para agregar metadatos a la imagen, como la información del mantenedor o la descripción extendida. Necesitamos instrucciones de LABEL para eso (anteriormente podríamos usar la opción MAINTAINER, pero ahora está en deprecated). Los metadatos a veces son utilizados por programas externos, por ejemplo, nvidia-docker requiere la etiqueta com.nvidia.volumes.needed para que funcione correctamente.

Ejemplo de metadatos en nuestro Dockerfile:
```
FROM node:7-alpine
LABEL maintainer "xxx@example.com"
...
```

# 14. Multistage

La utilización de `multietapas` (multistage builds) son una característica poderosa de Docker que permite crear imágenes más pequeñas y eficientes al usar múltiples etapas en un solo Dockerfile. 

Ejemplo:
[Multistage](/extras/04-mejorespracticas/)

```
# Etapa 1: Construcción
FROM node:10 as build
MAINTAINER Andres
LABEL description="This is a multi-stage NodeJS image"
WORKDIR /src
COPY package*.json .
RUN npm install
COPY . .

# Etapa 2: Producción
FROM node:10-slim
WORKDIR /src  
COPY --from=build /src .
EXPOSE 8080
CMD ["node", "index.js"]
```

