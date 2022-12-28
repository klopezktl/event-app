FROM python:3.9
EXPOSE 8080
WORKDIR /app
RUN pip install flask
COPY . /app
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8080"]