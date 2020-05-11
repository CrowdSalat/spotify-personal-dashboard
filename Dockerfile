FROM python:3.8-alpine

ENV ws /spotidash
RUN mkdir $ws
WORKDIR $ws

# prevents python from buffering when writing to stdout and stderr
ENV PYTHONUNBUFFERED 1 

# copy libraries first so it will be cached with docker layers if requirements.txt is not changed
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

# create database
RUN python manage.py migrate

ENTRYPOINT ["gunicorn","--bind", "0.0.0.0:8080", "config.wsgi"]
