# Actividad 6 - Conceptos avanzados de Docker 

## Actualización y desactualización de nuestra aplicación

El equipo de desarrollo Modernizacion ha creado una primera versión preliminar de una aplicación web y ha creado una imagen de contenedor con el siguiente nombre: `andr35/imagen:v0.1.0`.

Vamos a desplegar esta primera versión de la aplicación, para ello:

1. Crea un archivo yaml (manifiesto) para desplegar la imagen: `andr35/imagen:v0.1.0`.
2. Crea el Deployment, recuerda realizar una anotación para indicar las características del despliegue.
3. Crea una redirección utilizando el `port-forward` para acceder a la aplicación, sabiendo que la aplicación ofrece el servicio en el puerto 80, y accede a la aplicación con un navegador web.

Nuestro equipo de desarrollo ha seguido trabajando y ya tiene lista la versión 2 de nuestra aplicación, han creado una imagen que se llama: `andr35/imagen:v0.2.0`. Vamos a actualizar nuestro despliegue con la nueva versión, para ello:

1. Realiza la actualización del despliegue utilizando la nueva imagen (no olvides anotar la causa).
2. Comprueba los recursos que se han creado: Deployment, ReplicaSet y Pods.
3. Visualiza el historial de actualizaciones.
4. Crea una redirección utilizando el `port-forward` para acceder a la aplicación, sabiendo que la aplicación ofrece el servicio en el puerto 80, y accede a la aplicación con un navegador web.

Finalmente después de un trabajo muy duro, el equipo de desarrollo ha creado la imagen `andr35/imagen:v0.3.0` con la última versión de nuestra aplicación y la vamos a poner en producción, para ello:

1. Realiza la actualización del despliegue utilizando la nueva imagen (no olvides anotar "annotaions" de la causa).
2. Comprueba los recursos que se han creado: Deployment, ReplicaSet y Pods.
3. Visualiza el historial de actualizaciones.
4. Crea una redirección utilizando el `port-forward` para acceder a la aplicación, sabiendo que la aplicación ofrece el servicio en el puerto 80, y accede a la aplicación con un navegador web.

Sin embargo, está versión tiene un fallo, y no se ve de forma adecuada, por lo tanto, tenemos que volver a la versión anterior:

1. Ejecuta la instrucción que nos permite hacer un *rollback* de nuestro despliegue.
2. Comprueba los recursos que se han creado: Deployment, ReplicaSet y Pods.
3. Visualiza el historial de actualizaciones.
4. Crea una redirección utilizando el `port-forward` para acceder a la aplicación, sabiendo que la aplicación ofrece el servicio en el puerto 80, y accede a la aplicación con un navegador web.



Puede modificar la imagen, taguearla con una nueva versión, subirla a DockerHub y usarla en su propio manifiesto [Dockerfile](v0.3.0)



**Alternativas de despliegue**
- Cluster de k8s (EKS)/minikube/kind/k3s,etc
- Alternativa Killercoda
