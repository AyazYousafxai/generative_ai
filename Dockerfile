
FROM python:3.10


WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 80

ENV UVICORN_HOST=0.0.0.0 UVICORN_PORT=8080