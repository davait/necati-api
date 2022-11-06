# syntax=docker/dockerfile:1

FROM python:3.11-alpine

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
COPY *.py /app

RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip3 install -r requirements.txt

EXPOSE 9090
