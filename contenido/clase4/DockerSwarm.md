---
title: Docker
description: Fundamentos de docker IV
author: Claudio Andres Salamanca
tags: Docker, Introduccion
date_published: 2023-08-01
---


# ¿Qué es Docker Swarm?



Docker Swarm es una herramienta de orquestación de contenedores creada y administrada por Docker, Inc. Es la herramienta de agrupación en clústeres nativa de Docker. Swarm utiliza la API estándar de Docker, es decir, los contenedores se pueden iniciar utilizando comandos de ejecución normales de Docker y Swarm se encargará de seleccionar un host apropiado para ejecutar el contenedor. Esto también significa que otras herramientas que usan la API de Docker, como Compose y scripts personalizados, pueden usar Swarm sin ningún cambio y aprovechar la ejecución en un clúster en lugar de en un solo host.



## ¿Por qué necesitamos un orquestador?

Imagine que tuviera que ejecutar cientos de contenedores. Puede ver fácilmente que si se ejecutan en modo distribuido, hay varias funciones que necesitará desde el punto de vista de la administración para asegurarse de que el clúster esté en funcionamiento, en buen estado.

Algunas de estas características necesarias incluyen:

- Health checks de los contenedores
- Lanzar un conjunto fijo de contenedores para una imagen de Docker en particular
- Aumentar o reducir el número de contenedores según la carga
- Realizar actualizaciones continuas de software en todos los contenedores
- y más…<br>

Docker Swarm tiene capacidades para ayudarnos a implementar todas esas excelentes funciones, todo a través de CLI simples.



# ¿Cómo trabaja Docker Swarm? 

La arquitectura básica de Swarm es bastante sencilla: cada host ejecuta un agente Swarm y un host ejecuta un administrador Swarm (en grupos de prueba pequeños, este host también puede ejecutar un agente). El `manager` es responsable de la orquestación y programación de contenedores en los hosts. Swarm se puede ejecutar en un modo de alta disponibilidad donde se usa etcd, Consul o ZooKeeper para manejar la conmutación por error a un administrador de respaldo. Existen varios métodos diferentes para encontrar y agregar hosts a un clúster, lo que se conoce como `service descovery` en Swarm. De forma predeterminada, se utiliza el descubrimiento basado en tokens, donde las direcciones de los hosts se mantienen en una lista almacenada en Docker Hub.


Un swarm es un grupo de máquinas que ejecutan Docker y se unen en un clúster. Después de que eso haya sucedido, continuamos ejecutando los comandos de Docker a los que estamos acostumbrados, pero ahora son administrados por un `manager` de swarm que los ejecuta en un clúster. Las máquinas de un swarm  pueden ser físicas o virtuales. Después de unirse al swarm, se les denomina `nodos`.

Los administradores de swarm son las únicas máquinas de un swarm que pueden ejecutar sus comandos o autorizar a otras máquinas a unirse al swarm como `trabajadores`. Los `trabajadores` sólo están ahí para proporcionar capacidad y no tienen la autoridad para decirle a ninguna otra máquina lo que puede y no puede hacer.

Hasta ahora, has utilizando Docker en modo de host único en su máquina local. Pero Docker también se puede cambiar al modo `swarm`, y eso es lo que permite el uso de `swarm`. Habilitar el modo de `swarm` convierte instantáneamente a la máquina actual en un `manager` del swarm. A partir de ese momento, Docker ejecuta los comandos que ejecuta en el `swarm` que está administrando, en lugar de solo en la máquina actual.

Los `managers` del swarm  pueden usar varias estrategias para ejecutar contenedores, como el "nodo más vacío", que llena las máquinas menos utilizadas con contenedores. O "global", que garantiza que cada máquina obtenga exactamente una instancia del contenedor especificado.


![arquitectureDockerSwarm](./img/swarm_architecture.png)


En Docker Swarm, `servicio` y `tarea` son dos conceptos clave relacionados con la orquestación y ejecución de contenedores en un clúster. Veamos las diferencias entre ambos:

# Servicio:
Un servicio en Docker Swarm es una abstracción de alto nivel que define cómo se ejecutan los contenedores. Un servicio especifica una imagen base, opciones de configuración, escalabilidad y reglas de distribución. Los servicios son la unidad principal para la administración y orquestación de contenedores en un clúster Swarm. Los servicios permiten garantizar que un número específico de contenedores estén siempre en ejecución, lo que facilita la escalabilidad y la alta disponibilidad.

## Características claves de un servicio:

- Define la imagen del contenedor y la configuración.
- Puede tener varias tareas (instancias de contenedor) distribuidas en diferentes nodos.
- Se encarga de mantener el número deseado de réplicas, lo que garantiza la disponibilidad.
- Ofrece una dirección virtual y un nombre de servicio que se utiliza para acceder a las tareas a través de la red de `overlay`.


# Tarea:

Una tarea en Docker Swarm es una instancia individual de un contenedor que se ejecuta en un nodo específico dentro del clúster. Cada tarea representa la ejecución de una réplica de un servicio. Las tareas son las unidades más pequeñas de trabajo que se administran en un clúster Swarm. Docker Swarm se encarga de distribuir y balancear automáticamente las tareas en los nodos disponibles según las reglas definidas por el servicio.

## Características claves de una tarea:

- Es una instancia individual de un contenedor.
- Cada tarea representa una réplica de un servicio específico.
- Docker Swarm administra la distribución de tareas en los nodos según las reglas de distribución definidas por el servicio.
- Si una tarea falla, Docker Swarm la reiniciará en otro nodo según las políticas de disponibilidad definidas.


# Stack

Un stack se refiere a una colección de servicios que se definen e implementan juntos como una sola unidad.


Esto es especialmente útil cuando tienes una aplicación compuesta por varios servicios que trabajan juntos, como una aplicación web que incluye un frontend, un backend y una base de datos.

Un `stack` se define en un `docker-compose.yml`, que describe los servicios, las redes y otros elementos necesarios para ejecutar la aplicación completa. Luego, puedes implementar el `stack` de tareas en un clúster Docker Swarm utilizando el comando `docker stack deploy`.

# Ejemplo

[PlaywithDocker](https://www.docker.com/play-with-docker/)

 https://github.com/andres-dcic/dockerswarm