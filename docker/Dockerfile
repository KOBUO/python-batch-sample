FROM python:3.7-slim

RUN apt-get update -qq
RUN apt-get install -y gcc

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT 1

ADD . /var/www/html
WORKDIR /var/www/html

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system
