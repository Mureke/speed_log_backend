FROM python:3.8.1-buster

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
ENV FLASK_ENV = prod
ENV FLASK_APP = app.py
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD [ "deployment/docker_entry.sh" ]