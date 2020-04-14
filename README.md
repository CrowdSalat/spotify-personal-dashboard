# spotify-personal-dashboard

Dashboard for showing and clustering currently followed artists on spotify.

## authentication

1. [Create a client key](https://developer.spotify.com/documentation/general/guides/app-settings/). After creating you need to edit the [new client](https://developer.spotify.com/dashboard/applications)) and add a redirect uri.
2. Get new oauth2 access token with the [scopes](https://developer.spotify.com/documentation/general/guides/scopes/#user-read-private) you need.
   
```
Auth URL: https://accounts.spotify.com/authorize
Access Token URL: https://accounts.spotify.com/api/token
Redirect URI: {{callback_uri}}
Client ID: {{client_id}}
Client Secret: {{client_secret}}
Scope: playlist-read-private playlist-read-collaborative user-library-read user-follow-read user-top-read
Grant Type: Authorization Code
```

## python

### requirements

you need:

1. python 3
2. pip3 
3. modules defined in requirements.txt

### usage

- activate virtualenv `source env/bin/activate`
- install new packages via `pip install <packageName>` and afterwards save it in requirements.txt `pip3 freeze > requirements.txt`

### install (one time)

1. (optional) install pip3 if not present: `sudo apt-get install python3-pip` 
2. (optional) install virtualenv if not present: `sudo pip3 install virtualenv` (without sudo it wont be on the path)
3. checkout repo and navigate inside it: `git clone https://github.com/CrowdSalat/spotify-personal-dashboard.git && cd ./spotify-personal-dashboard` *(you may want to use ssh git url instead of the given https)*
4. Create virtualenv in root of this repo: `virtualenv env` (env is just the name)
5. Activate virtualenv: `source env/bin/activate`
6. Install python packages inside of the virtualenv: `pip3 install -r requirements.txt`

### misc

A nice working [python 2.7 example](https://developer.byu.edu/docs/consume-api/use-api/oauth-20/oauth-20-python-sample-code) for getting oauth token and accessing a oauth secured api.

## postman example

The project includes a postman project to explore the spotify api. In order to work:

1. import the spotify.postman_collection.json and the spotify.postman_environment.json files into postman
2. edit the spotify enviroment in postman so it includes your client_id and client_secret [see](#authentication)
3. under security generate a new oauth2 token and use it.

[Full guide](https://blog.postman.com/2016/11/09/generate-spotify-playlists-using-a-postman-collection/) from the official postman site explains how to configure a project in order to work with spotify api. 