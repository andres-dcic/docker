# Actividad 2 - Conceptos avanzados de Docker 

### Docker
1. Node >= 16 "alpine"
2. Crear un Dockerfile de la aplicacion app.js
3. Construir la imagen
4. Subir la imagen en el Registry docker-hub

### Kubernetes
1. Crear un manifiesto de kubernetes (pod), tomando en cuenta la imagen creada
2. nombre del objeto pod app-node
3. port 3000


```
apiVersion: apps/v1
kind: Pod
metadata:
  name: nodejs-app
spec:
  containers:
  - name: nodejs-container
    image: nodejs-app:latest
    ports:
      - containerPort: 3000
```

**Alternativas de despliegue**
- Cluster de k8s (EKS)/minikube/kind/k3s,etc
- Alternativa Killercoda
