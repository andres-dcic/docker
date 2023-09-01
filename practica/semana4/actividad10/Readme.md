# Actividad10 Conceptos avanzados de Docker

## Arquitectura de microservicios en Kubernetes

Desplegar  la actividad 1 de Docker Swarm en `Kubernetes`:

[VotingK8s](https://github.com/dockersamples/example-voting-app)

![arquitecture](./architecture.png)

La carpeta k8s-specifications contiene las especificaciones YAML de los servicios de la aplicación de voting.

Ejecute el siguiente comando para crear las implementaciones y los servicios. Tenga en cuenta que creará estos recursos en su espacio de nombres actual (`default`si no lo ha cambiado).

```shell
kubectl create -f k8s-specifications/
```

La aplicación web `vote` estará disponible en el puerto 31000 en cada host del clúster y  la aplicación web `result` estará disponible en el puerto 31001.


- *Aplicación de votación* basada en Python, que es una aplicación basada en UI donde agregará su voto.
- *Aplicación In Memory* basada en Redis que almacenará su voto en la memoria.
- *La aplicación Worker* , que es una aplicación basada en .net, convierte los datos de la memoria integrada en Postgres DB.
- *La aplicación Postgres DB* , que se basa en Postgres DB, recopila los datos y los almacena en la base de datos.
- *La aplicación de resultados* , que es una aplicación basada en la interfaz de usuario, obtiene los datos de la base de datos y muestra el voto a los usuarios.


**Alternativas de despliegue**
- Cluster de k8s (EKS)/minikube/kind/k3s,etc
- Alternativa Killercoda









