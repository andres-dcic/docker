# Actividad 9 - Conceptos avanzados de Docker 

## Labels


```
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
    - name: nginx-container
      image: nginx
```
Basado en el siguiente manifiesto, aplicar etiquetas a los nodos y los pods en un clúster, y luego realizar selecciones y filtrados basados en esas etiquetas.


- Aplicar una etiqueta a uno de los nodos como "ambiente=desarrollo"
- Ver las etiquetas de los nodos
- Aplicar una etiqueta al pod como "uso=prueba"
- Listar los nodos con la etiqueta "ambiente=desarrollo"
- Lista los pods con la etiqueta "uso=prueba
- Actualizar la etiqueta del pod "my-pod" a "uso=produccion"



**Alternativas de despliegue**
- Cluster de k8s (EKS)/minikube/kind/k3s,etc
- Alternativa Killercoda

