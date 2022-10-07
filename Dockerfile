FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get install -y \
    nginx           \
    nodejs          \
    npm             \
    build-essential \
    libssl-dev      

RUN useradd nginx

RUN mkdir -p /run/nginx

ENV TZ=America/Fortaleza
RUN cp /usr/share/zoneinfo/America/Fortaleza /etc/localtime
RUN echo "America/Fortaleza" > /etc/timezone

COPY ./requirements.txt /app/

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

COPY ./nginx.conf /etc/nginx/nginx.conf

# EXPOSE 8000