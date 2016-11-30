FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

RUN mkdir -p /etc/service/django
ADD djangoini.sh /etc/service/django
RUN echo `ls /etc/service/django`
RUN chmod -R 777 /etc/service/django
RUN sed -i "s/\r//" /etc/service/django/djangoini.sh
