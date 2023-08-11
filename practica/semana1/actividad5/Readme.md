# Actividad 5 - Fundamentos de docker I


## 1. Crea un contenedor con las siguientes especificaciones:

- Utilizar la imagen base NGINX haciendo uso de la version nginx:alpine
- Al acceder a la URL localhost:8080/index.html deberá aparecer el mensaje HOMEWORK
- Persistir el fichero index.html en un volumen llamado static_content


## 2. Crear el fichero Dockerfile. 

```bash
##Utilizar la imagen de nginx con la version requerida
FROM nginx:alpine
	
## Copiar el archivo index.htm de la carpeta src desde el host a la carpeta del contenedor
COPY /src/index.html /usr/share/nginx/html
```	

## 3. Crear un volumen 'static_content' en el CLI de Docker mediante la siguiente instruccion
```
docker volume create static_content 
```


## 4. Construir la imagen del contenedor. El nombre de la imagen es 'demo_container'
```
docker build -t demo_container . 
```
	

## 5. Crear el contenedor	con nombre 'bootcamp_container' utilizando la imagen construida en el paso 3

Mediante el parametro -v hacemos que el volumen 'static_content' creado en el paso 2 apunte al directorio del contenedor donde se encuentra el archivo index.html. De esta forma persistimos todo el contenido del directorio /usr/share/nginx/html del contenedor en el volumen

```
docker run -d --name demo_container -v static_content:/usr/share/nginx/html -p 8080:80 demo_container
```
	

## 6. Acceder a la URL http://localhost/8080/index.html y comprobar que aparece la página deseada


## 7. Sin detener el contenedor, modifique el index.html. ¿Cambió la página ?

## 8. Pushear a DockerHub 

- Recuerda que debes contar con una cuenta en https://hub.docker.com
- Logueate en docker-hub desde la terminal
- Ubicar el usuario de dockerhub, que con ese vas autheticarte
- Documentacion [Docker](https://docs.docker.com/engine/reference/commandline/login/)
```docker login````
```docker login -u "myusername" -p "mypassword" ```
- taguear la imagen
```
docker tag demo_container user_docker_hub/demo_container_nginx:v1.0.0 
```
- Push en el registry
```
docker push  user_docker_hub/demo_container_nginx:v1.0.0
```
- Listo!!

