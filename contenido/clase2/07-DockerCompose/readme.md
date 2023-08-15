---
title: Docker
description: Fundamentos de docker II
author: Claudio Andres Salamanca
tags: Docker, Introduccion
date_published: 2023-08-01
---

# Docker-compose
`Docker Compose` es la herramienta por excelencia para definir y ejecutar aplicaciones Docker de varios contenedores. Se utiliza un archivo en `formato yaml`  para configurar el ó los servicios de la aplicación. Luego, con un solo comando, crea e inicia todos los servicios desde su configuración. 

El uso de Compose es básicamente un proceso de tres pasos:

- Definir el entorno de su aplicación con un Dockerfile para que pueda reproducirse en cualquier lugar.
- Definir los servicios que componen su aplicación en docker-compose.yml para que puedan ejecutarse juntos en un entorno aislado.
- Por último, ejecutar docker-compose up, la cual desplegará todo el entorno para que la aplicación pueda funcionar.


# Ventajas de usar Docker-compose

* Hacer todo de manera **declarativa** para que no tenga que repetir todo el proceso cada vez que construyo el escenario.
* Poner en funcionamiento todos los contenedores que necesita mi aplicación de una sola vez y debidamente configurados.
* Garantizar que los contenedores **se arrancan en el orden adecuado**. Por ejemplo: mi aplicación no podrá funcionar debidamente hasta que no esté el servidor de bases de datos funcionando en marcha.
* Asegurarnos de que hay **comunicación** entre los contenedores que pertenecen a la aplicación.

# Instalación Docker-compose

Instalación de docker-compose  [Docker-compose](https://docs.docker.com/compose/install/)



# Introducción Docker-compose [v1]

## Archivo docker-compose

```bash
    version: "3"

    services: 
     redis:
      image: redis:alpine 
      volumes:
       - redis_data:/data
      restart: always

     mobycounter:
      depends_on:
       - redis
      image: russmckendrick/moby-counter
      ports:
       - "8080:80"
      restart: always
    
     volumes:
      redis_data:
```

Por ejemplo, si quisiera  implementara la misma aplicación, tendría que usar los siguientes comandos:

```
$ docker image pull redis:alpine
$ docker image pull russmckendrick/moby-counter
$ docker network create moby-counter
$ docker container run -d --name redis --network moby-counter redis:alpine
$ docker container run -d --name moby-counter --network moby-counter -p 8080:80 russmckendrick/moby-counter
```

Cada vez que necesitamos usar, actualizar, o instalar los contenedores en otro entorno deberíamos guardar, y gestionar todas las instrucciones, además tenemos que tener encuentra que comando debemos repetir, de ver si hace falta crear o no las redes de nuevo (por ejemplo).

Docker-compose  permite usar un archivo YAML para definir cómo le gustaría que se estructurara su aplicación de **múltiples** contenedores. Se tomaría el archivo YAML y se automatizaría el lanzamiento de los contenedores tal como se definió. La ventaja de esto fue que, debido a que era un archivo YAML, es muy fácil para los desarrolladores comenzar a enviar los archivos junto con sus archivos Docker dentro de sus bases de código.

Como ya se mencionó, Docker Compose usa un archivo YAML, normalmente denominado `docker-compose.yml`, para definir cómo debería verse su aplicación de múltiples contenedores.


Incluso sin trabajar a través de cada una de las líneas en el archivo, debe ser muy sencillo seguir adelante con lo que está sucediendo en. Para iniciar nuestra aplicación, simplemente cambie a la carpeta que contiene su archivo docker-compose.yml y ejecute lo siguiente: 

```bash
    $ docker-compose up
```

Como puede ver, desde las primeras líneas, Docker Compose hizo lo siguiente: 
- Creó una red llamada mobycounter_default usando el network1.driver predeterminado. En ninguna parte le pedimos a Docker Compose que hiciera esto.
- Creo un volumen llamado mobycounter_redis_data, nuevamente usando el controlador default2.driver. Esta vez le pedimos a Docker Compose que nos creara esta parte de la aplicación de múltiples contenedores.
- Lanzamos dos contenedores, uno llamado mobycounter_redis_1 y el segundo3.mobycounter_mobycounter_

La siguiente sección es donde se definen nuestros contenedores. Esta sección es la sección de servicios y  toma el siguiente formato:

```
    services:
    --> container name:
    ----> container options
    --> container name:
    ----> container options
```

En el siguiente link encontrará una aplicación bastante simple donde desplegar un CMD como Wordpress utilizando una base de datos en mysql, implementados mediante docker-compose. 
[Wordpress+Mysql](https://github.com/docker/awesome-compose/tree/master/wordpress-mysql)


# Docker Compose commands  [v1]

* `docker-compose up`: Crear los contenedores (servicios) que están descritos en el `docker-compose.yml`.
* `docker-compose up -d`: Crear en modo background los contenedores (servicios)en el `docker-compose.yml`.
* `docker-compose stop` : Detiene los contenedores que previamente se han lanzado con `docker-compose up`.
* `docker-compose run`  : Inicia los contenedores descritos en el `docker-compose.yml` que estén parados.
* `docker-compose rm`   : Borra los contenedores parados del escenario. Con las opción `-f` elimina también los contenedores en ejecución.
* `docker-compose pause`: Pausa los contenedores que previamente se han lanzado con `docker-compose up`.
* `docker-compose unpause`: Reanuda los contenedores que previamente se han pausado.
* `docker-compose restart`: Reinicia los contenedores. Orden ideal para reiniciar servicios con nuevas configuraciones.
* `docker-compose down`:  Para los contenedores, los borra  y también borra las redes que se han creado con `docker-compose up` (en caso de haberse creado).
* `docker-compose down -v`: Para los contenedores y borra contenedores, redes y volúmenes.
* `docker-compose logs`: Muestra los logs de todos los servicios del escenario. Con el parámetro `-f`podremos ir viendo los logs en "vivo".
* `docker-compose logs servicio1`: Muestra los logs del servicio llamado `servicio1` que estaba descrito en el `docker-compose.yml`.
* `docker-compose exec servicio1 /bin/bash`: Ejecuta una orden, en este caso `/bin/bash` en un contenedor llamado `servicio1` que estaba descrito en el `docker-compose.yml`
* `docker-compose build`: Ejecuta, si está indicado, el proceso de construcción de una imagen que va a ser usado en el `docker-compose.yml`  a partir de los  ficheros `Dockerfile` que se indican.
* `docker-compose top`: Muestra  los procesos que están ejecutándose en cada uno de los contenedores de los servicios.


- Crear los contenedores (servicios) que están en el `docker-compose.yml`.
``` bash
docker-compose up
# Nombrar el proyecto diferente a la carpeta:
# docker-compose -p mi-proy up -d
```

- Crear en modo background los contenedores (servicios) que están en el `docker-compose.yml`.
``` bash
docker-compose up -d
# Nombrar el proyecto diferente a la carpeta:
# docker-compose -p mi-proy up -d
```

- Detiene los contenedores que previamente se han lanzado con `docker-compose up`.
```bash
docker-compose stop
# docker-compose stop <servicio>
```
- Crear los contenedores (servicios) que están descritos en el `docker-compose.yml`.
``` bash
docker-compose start
# docker-compose start <servicio>
```
- Inicia los contenedores descritos en el `docker-compose.yml` que estén parados.
``` bash
docker-compose run
# docker-compose start <servicio>
```
- Para los contenedores, los borra  y también borra las redes que se han creado con `docker-compose up` (en caso de haberse creado).
``` bash
docker-compose down
# Eliminar los volumenes también:
# docker-compose --volumenes
# Eliminar con un nombre de proyecto específico:
# docker-compose -p mi-proy down
```
- Logs
``` bash
docker-compose logs
## docker-compose logs <servicio>
```
- Muestra los logs del servicio llamado `servicio1` que estaba descrito en el `docker-compose.yml`.
``` bash
docker-compose logs servicio1
```

- Ejecuta una orden, en este caso `/bin/bash` en un contenedor llamado `servicio1` que estaba descrito en el `docker-compose.yml`
``` bash
docker-compose exec servicio1 /bin/bash`
```

## Ejemplos Docker-compose

[Voting](https://github.com/dockersamples/example-voting-app)

[Wordpress](https://docs.docker.com/compose/wordpress/)

### - Algunos comandos útiles de Docker  [v1]
``` bash
## Ver contenedores
docker ps
## Ver imágenes
docker images
## Ingresar en un contenedores
 docker exec -it <nombre_contenedor> bash
## Ver logs de un contenedor
docker logs <nombre_contenedor> -f
## Eliminar imágenes huérfanas
docker rmi $(docker images -f "dangling=true" -q)

## Eliminar todas las imágenes  docker
docker rmi $(docker images -q)

## Eliminar todos los contenedores  docker
docker rm $(docker ps -a -q)
```


