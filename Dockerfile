FROM python:3.8-alpine

ENV ws /spotidash
RUN mkdir $ws
WORKDIR $ws

# copy libraries first so it will be cached with docker layers if requirements.txt is not changed
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080
# api keys + meldung falls diese nicht da sind

RUN python manage.py migrate

ENTRYPOINT ["gunicorn","--bind", "0.0.0.0:8080", "config.wsgi"]
