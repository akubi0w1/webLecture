FROM python:3.6

ENV PYTHONUNBUFFERED 1

ENV PYTHONIOENCODING utf-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP.UTF-8
ENV LC_ALL ja_JP.UTF-8

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/

RUN apt-get update \
    && apt-get install -y python3-dev
RUN pip install -r requirements.txt

