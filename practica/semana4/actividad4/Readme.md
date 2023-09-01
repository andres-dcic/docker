# Actividad 4 - Conceptos avanzados de Docker 

## Deployments

En esta actividad vamos a crear un Deployment de una aplicación web. Sigamos los siguientes pasos:

1. Crea un archivo yaml con la descripción del recurso Deployment, teniendo en cuenta los siguientes aspectos:
    * Indica nombres distintos para el Deployment y para el contenedor de los Pods que va a controlar.
    * El Deployment va a crear 2 réplicas.
    * La imagen que debes desplegar es `andr35/imagen:v0.2.0`.
    * Indica de manera adecuada una etiqueta en la especificación del Pod que vas a definir que coincida con el *selector* del Deployment.
2. Crea el Deployment.
3. Comprueba los recursos que se han creado: Deployment, ReplicaSet y Pods.
4. Obtén información detallada del Deployment creado.
5. Crea un una redirección utilizando el `port-forward` para acceder a la aplicación, sabiendo que la aplicación ofrece el servicio en el puerto 80, y accede a la aplicación con un navegador web.
6. Accede  a los logs del despliegue para comprobar el acceso que has hecho en el punto anterior.
7. Elimina el Deployment y comprueba que se han borrado todos los recursos creados.



**Alternativas de despliegue**
- Cluster de k8s (EKS)/minikube/kind/k3s,etc
- Alternativa Killercoda

