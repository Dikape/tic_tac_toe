FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
ADD . /app/

RUN rm -f /app/config.py

ENV APP_MODE=web
ENV FLASK_APP=./run.py