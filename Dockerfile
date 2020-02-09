FROM python:3.8.1-buster

ENV work_dir /app
RUN mkdir -p ${work_dir}

ENV FLASK_ENV = prod
ENV FLASK_APP = app.py

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev uwsgi supervisor


ADD requirements.txt ${work_dir}

RUN pip install uwsgi

WORKDIR /app

RUN pip install -r requirements.txt

COPY deployment/supervisor.ini /etc/supervisor.d/supervisor.ini

COPY . /app

EXPOSE 80 443

CMD [ "/app/deployment/docker-entry.sh" ]