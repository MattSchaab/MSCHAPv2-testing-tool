# Build backend
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8 AS backend

COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

WORKDIR /app
