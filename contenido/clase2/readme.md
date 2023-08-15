---
title: Docker
description: Fundamentos de docker II
author: Claudio Andres Salamanca
tags: Docker, Introduccion
date_published: 2023-08-01
---

# Fundamentos de docker II

En el contexto de Docker, `networking` se refiere a cómo los contenedores pueden comunicarse entre sí y con el mundo exterior. Docker proporciona varios tipos de redes que permiten diferentes grados de aislamiento y conectividad entre contenedores

Por otra parte, `Docker Compose` es una herramienta que facilita la definición y gestión de aplicaciones multi-contenedor en Docker. Permite definir toda la configuración de una aplicación en un archivo YAML llamado "docker-compose.yml". Este archivo contiene información sobre los contenedores que forman parte de la aplicación, sus configuraciones, volúmenes, variables de entorno y también puede incluir configuraciones de redes

El objetivo principal de utilizar Docker Compose en conjunto con la configuración de redes es simplificar la creación y administración de aplicaciones que constan de múltiples contenedores. Algunos de los beneficios clave incluyen:

`Definición declarativa`: Docker Compose permite definir la arquitectura de la aplicación y sus dependencias en un archivo YAML, lo que facilita la creación y replicación del entorno de desarrollo y producción.

`Facilita la comunicación`: Mediante la configuración de redes, Docker Compose facilita la comunicación entre los contenedores de la aplicación, lo que es esencial para las aplicaciones distribuidas.

`Gestión de recursos`: Docker Compose proporciona un mecanismo para asignar recursos de red a cada contenedor, controlando cómo se comunican y comparten información.

`Portabilidad`: La combinación de Docker Compose y las configuraciones de redes permite a los desarrolladores construir aplicaciones en entornos locales y luego desplegarlas de manera consistente en diferentes entornos, como entornos de prueba, etapas de preparación y producción.

 
- [Networking](/contenido/clase2/06-Networking/readme.md)
- [Docker-Compose](/contenido/clase2/07-DockerCompose/readme.md)


## Referencias:


Este repositorio toma prestado y adapta contenido de la siguiente fuente:
1. [Sitio oficial de Docker](https://docs.docker.com/)





