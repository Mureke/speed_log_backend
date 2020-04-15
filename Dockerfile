FROM python:3.7-buster

ENV work_dir /app
RUN mkdir -p ${work_dir}

ENV FLASK_ENV prod
ENV FLASK_APP /app/app.py

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev uwsgi supervisor libpq-dev python-psycopg2

RUN pip install psycopg2

ADD requirements.txt ${work_dir}

RUN pip install uwsgi
RUN pip install flask-sqlalchemy psycopg2

WORKDIR /app

RUN pip install -r requirements.txt

COPY deployment/supervisor.ini /etc/supervisor.d/supervisor.ini

COPY . /app

EXPOSE 80 443

CMD [ "/app/deployment/docker-entry.sh" ]