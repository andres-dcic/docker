# Actividad 1 - Desarrollo de aplicaciones con Docker


Los siguientes Dockerfiles presentan algunas malas prácticas. ¿Cómo los solucionaría? 

## Dockerfile1
```
FROM debian
COPY . /app
RUN apt-get update
RUN apt-get -y install openjdk-8-jdk
CMD ["java", "-jar", "/app/target/app.jar"]
``` 


## Dockerfile2
```
FROM debian
RUN apt-get update
RUN apt-get -y install openjdk-8-jdk
COPY target/ /app
CMD ["java", "-jar", "/app/target/app.jar"]
``` 



## Dockerfile3
``` 
FROM debian
RUN apt-get update && -y install \
    openjdk-8-jdk
COPY target/app.jar /app
CMD ["java", "-jar", "/app/target/app.jar"]
``` 



## Dockerfile4
```
FROM openjdk
COPY target/app.jar /app
CMD ["java", "-jar", "/app/target/app.jar"]
```


## Dockerfile5
```
# Etapa 1: Construcción
FROM python:3.8-slim as builder
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y build-essential
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 2: Imagen final
FROM python:3.8-slim
WORKDIR /app
COPY --from=builder /app /app
RUN apt-get remove --purge -y build-essential && apt-get autoremove -y
CMD ["python", "app.py"]
``` 


## Dockerfile6

```
FROM ubuntu:latest
RUN apt-get update && \
    apt-get install -y python3 python3-pip git vim curl && \
    apt-get clean
COPY . /app
RUN chmod +x /app/heavy_script.sh && /app/heavy_script.sh
EXPOSE 80 443 8080
CMD service apache2 start && service mysql start && tail -f /dev/null
``` 


## Dockerfile7
```
FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    vim \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]
``` 

## Dockerfile8
``` 
FROM ubuntu:latest
WORKDIR /
RUN apt-get update && \
    apt-get install -y vim curl && \
    apt-get clean
COPY . /
RUN /build_script.sh
EXPOSE 1-65535
ENV FOO=bar
CMD ["python", "app.py"]
```

## Dockerfile9

```
FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3 python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD python3 app.py
``` 


## Dockerfile10
```
FROM php:latest
RUN apt-get update && apt-get install -y \
    apache2 \
    php-mysql
COPY . /var/www/html
WORKDIR /var/www/html
CMD ["apache2ctl", "-D", "FOREGROUND"]
``` 








