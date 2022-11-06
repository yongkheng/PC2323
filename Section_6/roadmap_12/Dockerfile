FROM ubuntu:latest

RUN apt update && apt upgrade -y
RUN apt install -y -q build-essential python3-pip python3-dev
RUN pip3 install -U pip setuptools wheel
RUN pip3 install gunicorn uvloop httptools

RUN addgroup --system app && adduser --system --group app
RUN mkdir /code
WORKDIR /code

COPY ./app_repo/requirements.txt /code/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app_repo /code/app

WORKDIR /code/app
CMD gunicorn -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:80 main:api
