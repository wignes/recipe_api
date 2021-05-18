FROM python:3.8-alpine
MAINTAINER Vignesh Mayilsamy

ENV PYTHONBUFFERED 1
COPY Requirements.txt /Requirements.txt
RUN pip install -r /Requirements.txt
RUN mkdir /app
WORKDIR /app
COPY ./app /app
RUN adduser -D user
USER user
