# Actividad 4 - Fundamentos de docker I


## 1. Crear una imagen con un servidor web Apache y el contenido de la carpeta content (modificar el  Dockerfile de abajo)

```
docker build . -t simple-apache:new
```
## 2. Ejecutar el contenedor con la nueva imagen

```
docker run -d --name myapache -p 5050:80 simple-apache:new
```

## 2. Averiguar cuántas capas tiene la nueva imagen

```
docker inspect simple-apache:new #En el apartado "Layers" pueden contarse cuántas capas hay
docker history simple-apache:new #Todas las acciones que son < 0B son capas
docker image inspect simple-nginx -f '{{.RootFS.Layers}}'
```

Dockerfile

```
#Imagen que voy a utilizar como base
FROM nginx:alpine

#Etiquetado
LABEL project="AT Docker"

#Como metadato, indicamos que el contenedor utiliza el puerto 80
EXPOSE 80

#Modificaciones sobre la imagen que he utilizado como base, en este caso alpine
COPY content/ /usr/share/nginx/html/
```
