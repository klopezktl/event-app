# event-app
Event App

## Getting started
docker build -t event-app .
docker run -p 8080:8080 -w /app -v "$(pwd):/app" event-app

## Swagger-ui api documentation
http://localhost:8080/swagger-ui