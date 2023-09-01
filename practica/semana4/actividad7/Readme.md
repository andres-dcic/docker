# Actividad8 Conceptos avanzados de Docker


``` 
         +----------------------------+
         |       Ingress              |
         | (app.192.168.50.4.nip.io)  |
         +-----------|----------------+
                     |
                     v
          +-----------------------+
          |       Service         |
          |    (Nodeport  type)   |
          +-----------|-----------+
                      |
        +-------------|-----------------+
        v             v                 v
  +-------------+  +-------------+  +-------------+
  | Deployment  |  | Deployment  |  | Deployment  |
  |(Pod Replica |  |(Pod Replica |  |(Pod Replica |
  |   1, 2, 3)  |  |   1, 2, 3)  |  |   1, 2, 3)  |
  +-------------+  +-------------+  +-------------+
``` 


- Despliegue la siguiente arquitectura de nginx basado en el deployment->service->ingress 



**Alternativas de despliegue**
- Cluster de k8s (EKS)/minikube/k3s/etc
- Alternativa Killercoda
