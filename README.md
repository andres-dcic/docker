# AT Docker - Secretaría de modernización de Catamarca 08/23 


## Objetivo
El objetivo general de esta asistencia técnica es proporcionar a la Secretaría de  Modernización capacidades y herramientas para abordar los aspectos prácticos de `Docker`,
a fin de que la institución pueda contar con las habilidades necesarias para la gestión adecuada de la plataforma. 

Específicamente, se busca que el cuerpo de agentes vinculados a la AT puedan crear y desplegar aplicaciones utilizando contenedores Docker, comprendiendo los pasos necesarios para empaquetar una aplicación en una imagen `Docker`, configurar su entorno y ejecutarlo de manera consistente en diferentes entornos.


## Contenido

### [01 - Fundamentos de docker I ](./contenido/clase1/00-motivacion/readme.md)

<!--
- Instalación de los componentes necesarios para utilizar Docker
- Pull y Push de una imagen
- Container Registry/Docker Registry
-->

- ¿Qué es Docker y por qué se utiliza?
- Arquitectura y componentes de Docker 
- Ejecutar tu primer contenedor de Docker
- Comandos básicos de Docker
- Construir imágenes de Docker con Dockerfiles
- Gestión de datos con volúmenes de Docker y bind mounts
- Publicación y descarga de imágenes en Docker Hub
- [Ejercicios](./practica/semana1/)

### 02 - Fundamentos de docker II
<!--
- Crear una imagen a partir de una aplicación propia
- Tagging de imágenes
- Update de imágenes
- Correr varias instancias de la misma imagen
- Balanceando tráfico a las imágenes
-->

- Conceptos de networking en Docker 
- Exponer puertos y acceder a servicios en contenedores de Docker
- Comunicación entre contenedores y enlaces de contenedores
- Uso de Docker Compose para definir y gestionar aplicaciones multicontenedor
- [Ejercicios](./practica/semana2/)


### 03 - Desarrollo de aplicaciones
<!--
- Instalación de Kubernetes en local
- Primera prueba de pod
- Nuestra app en un pod
- Exponer y probar nuestra aplicación
- Formas de exponer servicios
-->

- Dockerización de diferentes tipos de aplicaciones 
- Mejores prácticas para escribir Dockerfiles y optimizar imágenes de Docker
- Contenerización de aplicaciones heredadas con Docker
- Uso de Docker en pipelines de CI/CD
- Mejores prácticas de seguridad para contenedores de Docker
- [Ejercicios](./practica/semana3/)

### 04 - Docker Swarm / Kubernetes

<!--
- Self-healing
- Controladores
- Balanceo por medio de servicio
- Multiples servicios, mismo label
-->

- Introducción a Docker Swarm y Kubernetes
- Configuración de un clúster de Docker Swarm
- Implementación de servicios y escalado de contenedores con Docker Swarm
- Conceptos de Kubernetes (pods, deployments, services, etc.)
- Implementación de aplicaciones y escalado de contenedores con Kubernetes
- [Ejercicios](./practica/semana4/)

<!--
### [05 - Buenas prácticas](contenido/05-buenas-practicas.md)

- Namespaces
- Kustomization
- Herramientas
- Aplicar resources al spec
- SecurityContext
- Optimizar imagen
  - Tamaño
  - Layers
  - Alpine
- Readiness, Liveness
  
### [06 - Monitoreo](contenido/06-monitoreo.md)

- Prometheus
  - Queries
- Grafana
  - Dashboards públicos

### [07 - Resolución de problemas](contenido/07-troubleshooting.md)

- Ejemplos de situaciones comunes
  - CrashLoopBackOff
  - ImagePullBackOff
  - Pending
  - OOMKill
  - Readiness
  - Terminating
- kubectl explain
- kubectl debug
- Operadores y su complejidad

### [99 - Cheatsheet](contenido/99-cheatsheet.md)

- K3d
- Docker
- Kubernetes

## Otros recursos

- [kube.academy](https://kube.academy/)
- [kube.campus](https://kubecampus.io/)

## Comandos para el workshop en vivo

En un archivo [dejamos todos los comandos](contenido/00-comandos.md) que se utilizarán durante el workshop para que puedan copiar y pegar acorde a como vayan avanzando en el material.
-->
