# Actividad 2- Desarrollo de aplicaciones con Docker

## Simple microservicio con Docker

El directorio /app contiene un pequeño microservicio Python Dockerizado al que llamaremos `service`. Tiene un único punto final,`value`, con la siguiente API. * GET /value devuelve un objeto JSON con el valor clave establecido en el valor actual (una cadena). * POST /value donde se establecerá el valor actual.

De acuerdo al Dockerfile, deberá crear un `docker-compose.yml` que comunique el microservicio escuchando en el 8080 y una base de datos no relacional (redis) escuchando en el 6379 donde almacene el valor

Para probar la api puede utilizar curl ó postman 
```
$ curl http://localhost:8080/value
{"value": "None"}
$ curl -X POST http://localhost:8080/value -H "Content-Type: application/json" -d '{"value": "prueba"}'
$ curl http://localhost:8080/value
{"value": "prueba"}
```


