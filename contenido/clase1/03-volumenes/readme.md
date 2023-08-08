---
title: Docker
description: Fundamentos de docker I
author: Claudio Andres Salamanca
tags: Docker, Introduccion
date_published: 2023-08-01
---

# Volumenes

Una de las mas importantes funcionalidades de Docker son los volúmenes.

Estos no son mas que carpetas en nuestro sistema de ficheros que son capaces de sobrevivir al ciclo de vida normal del contenedor. Los volúmenes suponen el modo en el que Docker permite persistir los datos de tu aplicación. Los aloja fuera del propio contenedor, en el propio sistema de archivos del host donde está corriendo Docker, de tal manera que se puede cambiar, apagar o borrar el contenedor sin que afecte a los datos.


![volumenes](img/volumes.jpg)

Los volúmenes son bastante útiles porque permiten compartirse entre contenedores, o el propio host. Eso nos permite cosas como:

- Montar el código fuente de una aplicación web, dentro de un volumen, accesible desde el contenedor web y así ver en tiempo real los cambios durante el desarrollo.

- Consultar todos los logs cómodamente desde un contenedor dedicado.

- Hacer backups de un contenedor desde otro dedicado, o recuperar esos mismo backups hacia nuestro host.

- Compartir la misma información entre varios contenedores sin duplicarla. Por ejemplo la información relativa al entorno: desarrollo, integración, preproducción, producción.

De hecho, se pueden hacer contenedores con la única función de producir ficheros (.tar.gz, .deb, …) en volúmenes que luego son consumidos por servicios de runtime, por ejemplo un servidor web, un repositorio o simplemente un NFS. Para ello hay que definir qué parte del contenedor se dedica a la aplicación y qué parte a los datos.

- Los volúmenes de datos están diseñados para conservar los datos, independientemente del ciclo de vida del contenedor.

- Docker, por lo tanto, `nunca elimina automáticamente` los volúmenes cuando se elimina un contenedor, ni tampoco “recoge basura”: volúmenes huerfanos a los que ya no hace referencia un contenedor.

- Los volúmenes son específicos de cada contenedor, es decir, que puedes crear n contenedores a partir de una misma imagen y definir volúmenes diferentes para cada uno de ellos:

- Los volúmenes también pueden usarse para compartir información entre contenedores.Montar el código fuente de una aplicación web, dentro de un volumen, accesible desde el contenedor web y así ver en tiempo real los cambios durante el desarrollo.

- Consultar todos los logs cómodamente desde un contenedor dedicado.

- Hacer backups de un contenedor desde otro dedicado, o recuperar esos mismo backups hacia nuestro host.

- Compartir la misma información entre varios contenedores sin duplicarla. Por ejemplo la información relativa al entorno: desarrollo, integración, preproducción, producción.

## Tipos de Volúmenes

Los volúmenes pueden ser de 3 tipos distintos, y se categorizan según esta lista:

- `Data volumes`
    - Anonymous data volumes
    - Named data volumes
- `Mounted volumes`

## Data volumes (Volumes de docker)
### Anonymous data volumes
Se crean cuando se levanta un contenedor y no se le asigna un nombre concreto, mediante el comando docker run, por ejemplo:

```bash
docker run -ti --name alpine1 --rm -v /data alpine:3.4 sh
```


A su vez, otro contenedor puede montar los volúmenes de otro contenedor, ya sea porque los creó o porque los ha montado de un tercero.
```bash
docker run -ti --name alpine2 --rm --volumes-from alpine1 alpine:3.4 sh
```

### Named data volumes

Estos volúmenes no dependen de ningún contenedor concreto, y se pueden montar en cualquier contenedor. Se crean específicamente usando el comando docker volume create, o al ejecutar un contenedor si le damos un nombre en la línea de comandos.

```bash
docker volume create --name vol1
vol1
docker run -ti --rm -v vol2:/data alpine:3.4 true
docker volume ls
DRIVER              VOLUME NAME
local               vol1
local               vol2
```
Estos volúmenes no se eliminan por si solos nunca y persisten cuando su contenedor desaparece. Para eliminarlos se necesita una intervención manual mediante el comando docker volume rm.

## Mounted volumes  (Bind)

Otras veces nos interesa montar archivos o carpetas desde la máquina host. En este caso, podemos montar la carpeta o el fichero especificando la ruta completa desde la máquina host, y la ruta completa en el contenedor. Es posible también especificar si el volumen es de lectura y escritura (por defecto) o de solo lectura.

```bash
$ docker run -ti --rm -v /etc/hostname:/root/parent_name:ro -v /opt/:/data alpine:3.4 sh
$ cat /root/parent_name
$ ls /data/
```

Este último caso es ideal para recuperar *backups* o ficheros generados en un contenedor, en vistas a su utilización futura por parte de otros contenedores o del mismo *host*.

# Tocando los Volumenes

Con los volumenes tenemos la manera sencilla y predefinida para almacenar todos los archivos (salvo unas pocas excepciones) de un contenedor, usará el espacio de nuestro equipo real y en “/var/lib/docker/volumes” creará una carpeta para cada contenedor.

Podemos crear un volúmen con un nombre especial (que pueda facilitar su gestión) o dejar que el propio Docker le asigne un “hash”.

Ahora creamos un volúmen llamado “mis_datos”.

```bash
docker volume create mis_datos
``` 

Veremos las propiedades de ese volúmen y donde está almacenado en nuestro equipo real “/var/lib/docker/volumes/mis_datos/_data”.

```bash
docker volume inspect my-vol
```

También podremos eliminar ese volúmen con la opción “rm”.
```bash
docker volume rm mis_datos
```
Hasta que no borremos los contenedores que usen ese volúmen, no podremos borrarlo.


Ejemplo de creación de un nuevo contenedor usando ese volúmen, asociándolo a la carpeta “/var/lib/mysql” del contenedor.

```bash
docker run -d -it --name ubu1 -v mis_datos:/var/lib/mysql ubuntu:17.10
# Otro ejemplo
docker run -d -v $(pwd)/data:/data awesome/app bootstrap.sh

# También es posible usar una refencia relativa a la carpeta donde estémos parados al correr la creación del contenedor. (pwd)
```bash
docker run -d -it --name ubu2 -v "$(pwd)"/datos:/var/lib/mysql ubuntu:17.10
```

El comando inspect del contenedor nos dará mas información sobre la unidad montada. En este caso la carpeta “/tmp/datos” se montará como “/var/lib/mysql” en el contenedor. Indica que el acceso es R/W (lectura y escritura).

```bash
docker inspect ubu2
```



TMPFS (temporal file system) es una manera de montar carpetas temporales en un contenedor.

Usan la RAM del equipo y su contenido desaparecerá al parar el contenedor.

En caso de tener poca RAM, los ficheros se parasán al SWAP del equipo real.

Crearemos otro contenedor donde una determinada carpeta de un servidor web será “temporal”.

```bash
docker run -d -it --name ubu3 --tmpfs /var/html/tempo ubuntu:17.10
```
Salvo que indiquemos una limitación de espacio usando el modificador “tmpfs-size=999bytes”, el espacio que pueden ocupar los ficheros es ilimitado (o limitado por el espacio disponible de RAM)

Este tipo de almacenamiento puede ser usado para almacenar ficheros de sesiones web, temporales o contenido que nos interese que se borre en cada rearranque del contenedor.

