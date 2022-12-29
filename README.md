# event-app
Event App

## Getting started - HOST
`docker build -t event-app .`

`docker run -p 8080:8080 -w /app -v "$(pwd):/app" event-app`

## Getting started - WEB
`cd event-web`
`npm i`
`ng serve`

## Swagger-ui api documentation
http://localhost:8080/swagger-ui