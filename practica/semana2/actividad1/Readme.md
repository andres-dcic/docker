# Actividad 1 - Fundamentos de docker II

El siguiente script es utilizado para levantar un gestor de contenido como Wordpress que necesita de una base de datos para funcionar


```
#!/bin/bash
set -e
docker pull wordpress:latest
docker images | grep wordpress
docker pull mysql:latest
docker images | grep mysql
docker run --name mysqlwp -e MYSQL_ROOT_PASSWORD=wordpressdocker -d mysql
docker run --name wordpress --link mysqlwp:mysql --rm -d -p 8002:80 wordpress

```

- Analice las distintas líneas del script anterior e intente armar un `docker-compose.yml` para que el gestor de contenido pueda funcionar en
 el puerto 8002 del docker host.
