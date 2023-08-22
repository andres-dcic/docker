
FROM node:10 as build
MAINTAINER andres
LABEL description="This is a multi-stage NodeJS image"
WORKDIR /src
COPY package*.json .
RUN npm install build
COPY . .

FROM node:10-slim
WORKDIR /src 
COPY --from=build /src .
EXPOSE 8080
CMD ["node", "index.js"]
