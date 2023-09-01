# Actividad 3 - Conceptos avanzados de Docker 

## ReplicaSet

1. Crea un archivo yaml con la descripción del recurso ReplicaSet, teniendo en cuenta los siguientes aspectos:
    * Indica nombres distintos para el ReplicaSet y para el contenedor de los Pods que va a controlar.
    * El ReplicaSet va a crear 3 réplicas.
    * La imagen que debes desplegar es `andr35/imagen:v0.1.0`.
    * Indica de manera adecuada una etiqueta en la especificación del Pod que vas a definir que coincida con el *selector* del ReplicaSet.
2. Crea el ReplicaSet.
3. Comprueba que se ha creado el ReplicaSet y los 3 Pods.
4. Obtener información detallada del ReplicaSet creado.
5. Probar la tolerancia a fallos: Eliminar uno de los 3 Pods, y comprueba que inmediatamente se ha vuelto a crear un nuevo Pod.
6. Comprobar la escalabilidad: escala el ReplicaSet para tener 6 Pods de la aplicación.
7. Eliminar el ReplicaSet y comprueba que se han borrado todos los Pods.


**Alternativas de despliegue**
- Cluster de k8s (EKS)/minikube/kind/k3s,etc
- Alternativa Killercoda


