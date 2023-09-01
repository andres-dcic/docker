# Actividad 1 - Conceptos avanzados de Docker 

1. Acceda a [Playwithdocker](https://labs.play-with-docker.com/) y despliegue un minicluster en `Docker Swarm con 1 manager y 1 trabajador`

2. Baje el siguiente repositorio https://github.com/dockersamples/example-voting-app

```
   - *La aplicación vote* basada en Python, es una aplicación basada en UI donde agregará su voto.
   - *La aplicación Redis* basada en Redis que almacenará su voto en la memoria.
   - *La aplicación Worker* , que es una aplicación basada en .net, convierte los datos de la memoria integrada en Postgres DB.
   - *La aplicación Postgres DB* , que se basa en Postgres DB, recopila los datos y los almacena en la base de datos.
   - *La aplicación Result* , que es una aplicación basada en la interfaz de usuario, obtiene los datos de la base de datos y muestra el voto a los usuarios.
```

3. Sobre el host manager despliegue el stack de servicios del archivo `docker-stack.yaml` 

4. Analice la arquitectura de microservicios como se comunican

5. Intente escalar el servicio de `vote` a 5 instancias



