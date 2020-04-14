#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Example for calling the sporitfy api with oauth2 via python3. 
You need to register your app as described here: https://developer.spotify.com/documentation/general/guides/app-settings/
Do not forget to add the callback_uri "http://localhost" to your newly registered app in the spotify dashboard.
Initialize the client_id and the client_secret with the values from your app in the spotify dashboard
"""

import requests
import json
import subprocess
import sys


authorize_url = "https://accounts.spotify.com/authorize"
token_url = "https://accounts.spotify.com/api/token"

# application defined under https://developer.spotify.com/dashboard/
callback_uri = "http://localhost"
client_id = '----------- fill in your clientid> -----------'
client_secret = '----------- fill in your secret clientid -----------'

# spotify scopes: https://developer.spotify.com/documentation/general/guides/scopes/#user-read-private
scope_query = '&scope='


test_api_url = "https://api.spotify.com/v1/me/following?type=artist"


def define_scope(scope: str, *scopes):
    global scope_query
    scope_query += scope
    for scopeItem in scopes:
        scope_query += "+"
        scope_query += scopeItem


def request_access_code():
    authorization_redirect_url = authorize_url + '?response_type=code&client_id=' + \
        client_id + '&redirect_uri=' + callback_uri + scope_query
    print("open the url in the browser and enter the code which is in the returned url (?code=...): ")
    print("***  " + authorization_redirect_url + "  ***")
    authorization_code = input('code: ')
    return authorization_code


def request_access_token(authorization_code):
    data = {
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': callback_uri
    }
    print("requesting access token")
    access_token_response = requests.post(
        token_url, data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret))
    print("response")
    print('header: ' + str(access_token_response.headers))
    print('body: ' + str(access_token_response.text))
    tokens = json.loads(access_token_response.text)
    access_token = tokens['access_token']
    print("access token: " + access_token)
    return access_token


scope = ["playlist-read-private", "playlist-read-collaborative",
         "user-library-read", "user-follow-read", "user-top-read"]
define_scope(*scope)
access_code = request_access_code()
access_token = request_access_token(access_code)

api_call_headers = {'Authorization': 'Bearer ' + access_token}

api_call_response = requests.get(
    test_api_url, headers=api_call_headers, verify=False)


print("---------------------------")
print("status_code")
print(api_call_response.status_code)

print("response")
print(api_call_response.text)
