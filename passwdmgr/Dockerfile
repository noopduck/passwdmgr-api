FROM python:3.9
ENV PYTHONUNBUFFERED=1
RUN mkdir -p /code/static
WORKDIR /code
RUN python3 -m venv env
ADD requirements.txt /code/
ADD . /code/
RUN pip install -r requirements.txt
RUN apt-get update -y && apt-get install apt-utils -y && apt-get upgrade -y
RUN groupadd django; useradd -s /bin/bash -g django -d /code django
RUN chown -R django.django /code
RUN cd /code; python manage.py collectstatic --noinput
#EXPOSE 8000
#ENTRYPOINT ["/code/gunicorn_start"]
