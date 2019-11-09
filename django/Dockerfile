FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV LANG en_US.utf8

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/

RUN apt-get update \
    && apt-get install -y python3-dev
RUN pip install -r requirements.txt

