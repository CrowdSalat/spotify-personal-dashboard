# spotify-personal-dashboard

Dashboard for showing and clustering currently followed albums on spotify.

## TODO

- nicer cards and layouts via css
- better routing with exception handling
- more than 20 resutls maybe via paging
- searching and filtering

## development

### run

- activate environment: `source env/bin/activate`
- start django development server on 8080: `python manage.py runserver 8080`

### requirements

you need:

1. python 3
2. pip3 
3. modules defined in requirements.txt

### update packages

- activate virtualenv `source env/bin/activate`
- install new packages via `pip install <packageName>` and afterwards save it in requirements.txt `pip3 freeze > requirements.txt`

### install (one time)

1. (optional) install pip3 if not present: `sudo apt-get install python3-pip` 
2. (optional) install virtualenv if not present: `sudo pip3 install virtualenv` (without sudo it wont be on the path)
3. checkout repo and navigate inside it: `git clone https://github.com/CrowdSalat/spotify-personal-dashboard.git && cd ./spotify-personal-dashboard` *(you may want to use ssh git url instead of the given https)*
4. Create virtualenv in root of this repo: `virtualenv env` (env is just the name)
5. Activate virtualenv: `source env/bin/activate`
6. Install python packages inside of the virtualenv: `pip3 install -r requirements.txt`

## authentication overview

steps:

1. [Create a client key](https://developer.spotify.com/documentation/general/guides/app-settings/). After creating you need to edit the [new client](https://developer.spotify.com/dashboard/applications)) and add a redirect uri.
2. Get new oauth2 access token with the [scopes](https://developer.spotify.com/documentation/general/guides/scopes/#user-read-private) you need.
   
- The spotify [developer dashboard](https://developer.spotify.com/dashboard/login) for managing your api keys.
- oauth python clients:
  - [python 2.7 example](https://developer.byu.edu/docs/consume-api/use-api/oauth-20/oauth-20-python-sample-code) 
  - [python 3 example for spotify](https://gist.github.com/CrowdSalat/770bb1b5a1a8c892b37b7fd940a8e133)
 
```
Auth URL: https://accounts.spotify.com/authorize
Access Token URL: https://accounts.spotify.com/api/token
Redirect URI: {{callback_uri}}
Client ID: {{client_id}}
Client Secret: {{client_secret}}
Scope: playlist-read-private playlist-read-collaborative user-library-read user-follow-read user-top-read
Grant Type: Authorization Code
```

## django

- django was scaffolded with commands:  
  - `django-admin startproject config` create django project named config
  - `python manage.py startapp dashboard` create django app inside of django porject named config
  - `python manage.py migrate` created the standard database tables for django. Needed for session.
- django docs:
  - [official starting django tutorial](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)
  - [how to handle django project with one django app](https://learndjango.com/tutorials/django-best-practices-projects-vs-apps)

## postman example

The project includes a postman project to explore the spotify api. In order to work:

1. import the spotify.postman_collection.json and the spotify.postman_environment.json files into postman
2. edit the spotify enviroment in postman so it includes your client_id and client_secret [see](#authentication)
3. under security generate a new oauth2 token and use it.

[Full guide](https://blog.postman.com/2016/11/09/generate-spotify-playlists-using-a-postman-collection/) from the official postman site explains how to configure a project in order to work with spotify api. 