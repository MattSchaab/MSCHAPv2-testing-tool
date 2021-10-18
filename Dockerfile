# Build frontend
FROM node:16-alpine3.11 AS frontend
WORKDIR /app
ADD ./frontend/ /app/
RUN npm install --production
RUN npm run build

# Build backend
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8 AS backend
WORKDIR /app
ADD ./backend/ /app/

RUN pip install -r requirements.txt

ENV APP_MODULE="main:app"