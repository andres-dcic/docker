---
title: Docker
description: Fundamentos de docker III
author: Claudio Andres Salamanca
tags: Docker, Introduccion
date_published: 2023-08-01
---

# Seguridad en Docker

La seguridad en Docker es una `consideración crucial`, ya que los contenedores comparten el mismo sistema operativo del host y, si no se configuran adecuadamente, podrían exponer vulnerabilidades. Aquí hay algunas prácticas y enfoques clave para mejorar la seguridad en Docker:


**Utilizar Imágenes Oficiales y Confiables:**
Prefiere imágenes oficiales o de confianza desde repositorios como Docker Hub. Evita imágenes desconocidas o no verificadas.

**Mantener Imágenes y Contenedores Actualizados:**
Regularmente actualiza tus imágenes y contenedores para aplicar parches de seguridad y correcciones. Utiliza imágenes base con versiones actualizadas.

**Minimiza el contenido de las imágenes:**
Reduce el tamaño y las superficies de ataque eliminando paquetes y dependencias innecesarias de tus imágenes.

**Crea usuarios y grupos Separados:**
No ejecutes contenedores con privilegios de root. Crea usuarios y grupos específicos en tu Dockerfile y configura el contenedor para ejecutarse con esos permisos.

**Utiliza Docker Bench Security:**
Esta herramienta de código abierto verifica la configuración de seguridad de tus entornos Docker y ofrece recomendaciones para mejorarla.

**Controla los Recursos del Contenedor:**
Limita los recursos (CPU, memoria) que un contenedor puede consumir para prevenir un uso excesivo.

**Limita Capabilities:**
Restringe las capacidades del contenedor a lo estrictamente necesario para reducir posibles vectores de ataque.

**Aísla los Contenedores con Redes y Volúmenes:**
Utiliza redes y volúmenes para aislar los contenedores y limitar su exposición a otros contenedores y al host.

**Implementa Firewalls y Seguridad de Red:**
Aplica reglas de firewall y segmentación de red para limitar la comunicación entre contenedores y hosts.

**Utiliza Docker Content Trust y Notary:**
Habilita Docker Content Trust para verificar la autenticidad y origen de las imágenes. Docker Notary proporciona una plataforma para firmar y verificar imágenes.

**Monitorea y Audita:**
Implementa monitoreo y auditoría para detectar y responder a eventos de seguridad en contenedores y clústeres.

**Limita el Acceso a los Sockets del Host:**
Controla el acceso a los sockets del host a través de la configuración adecuada de los volúmenes y los enlaces de socket.

**Emplea Herramientas de Seguridad:**
Utiliza herramientas de seguridad como Clair para escanear imágenes en busca de vulnerabilidades conocidas.

**Considera Soluciones de Orquestación Segura:**
Si usas Kubernetes o Swarm, implementa medidas de seguridad específicas para las soluciones de orquestación.

**Educación y Concienciación:**
Asegúrate de que tu equipo de desarrollo y operaciones estén capacitados en las mejores prácticas de seguridad de Docker.


# Ejemplo

Docker es una tecnología de contenedores ampliamente utilizada y es importante saber cómo implementar y utilizar Docker de forma segura. 

Supongamos que un usuario en el sistema no tiene permiso para ejecutar `sudo` (no tiene privilegios de administrador), pero sí tiene permiso para ejecutar contenedores Docker.

Analicemos el siguiente ejemplo:

```
$ echo "top secret" | sudo tee /root/secret.txt

$ sudo chmod 0600 /root/secret.txt

$ sudo ls -al /root/secret.txt

-rw------- 1 root root 11 Apr 16 15:00 /root/secret.txt

$ sudo cat /root/secret.txt

top secret

$ cat /root/secret.txt

cat: cannot access '/root/secret.txt': Permission denied
```

Pero qué pasa si se ejecuta docker de está forma: 

```
docker run --rm -v /root/secret.txt:/tmp/secret.txt alpine:latest cat /tmp/secret.txt
```


Aunque el comando se ejecutó como un usuario no root, el proceso se ejecuta como root dentro del contenedor y, por lo tanto, puede acceder a un archivo al que solo puede acceder root. De manera similar, se podría montar todo el sistema de archivos del host en el contenedor y leer y escribir cualquier archivo de la misma manera. `Muy peligroso`

Lo importante aquí es que el usuario raíz dentro del contenedor y el usuario raíz en el host son en realidad el mismo usuario. Por lo tanto, si el aislamiento del contenedor falla por cualquier motivo, ya sea por una configuración incorrecta o por un exploit que permite salir del contenedor, podría otorgar al proceso privilegios de raíz en el host.


Para mayor información de como evitar esto: [Aislar los contenedores con un namespace de usuario](https://docs.docker.com/engine/security/userns-remap/)