FROM python:3.7.6-slim

RUN apt-get update && apt-get install -y libgl1-mesa-glx && apt-get install -y apt-utils && apt-get install -y gcc && apt-get install -y cmake && apt-get install -y apache2 && apt-get install -y apache2-dev && apt-get clean && apt-get autoremove && rm -rf /var/lib/apt/lists/* && apt-get update && apt-get install -y emacs

COPY requirements.txt /
RUN pip install -r /requirements.txt

EXPOSE 8080

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

WORKDIR /var/www/FlaskApp/
COPY ./flask.wsgi /var/www/FlaskApp/flask.wsgi
COPY ./FlaskApp /var/www/FlaskApp/

RUN mod_wsgi-express install-module
RUN mod_wsgi-express setup-server flask.wsgi --port=8080 \
    --user www-data --group www-data \
    --server-root=/etc/mod_wsgi-express-80

CMD /etc/mod_wsgi-express-80/apachectl start -D FOREGROUND