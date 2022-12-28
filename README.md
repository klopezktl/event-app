# event-app
Event App

pip install -r requirements.txt
export FLASK_RUN_PORT=8080
docker build -t event-app .
docker run -p 8080:8080 event-app

pip install -r requirements.txt


docker build -t event-app .
docker run -dp 8080:8080 -w /app -v "$(pwd):/app" event-app