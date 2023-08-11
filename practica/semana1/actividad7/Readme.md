# Actividad 7 - Fundamentos de docker I


El siguiente `Dockerfile` está incompleto y debe modificarse para producir los resultados siguientes.
(`Sugerencia, es posible que deba agregar una variable de entorno`).

## 1. Construir la imagen 
```
docker build -t testimage .
```

## 2. Correr y setear la variable de entorno `myhost`
```
docker run -e myhost=host1 testimage
```

## 3. Deberías ver la siguiente salida
```
    host1
```

## 4. Sin ninguna variable de entorno tú deberías ver la siguiente salida
```
    docker run testimage

    testhost
```

