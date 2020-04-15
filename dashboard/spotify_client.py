import requests
import json
import subprocess
import sys


class SpotifyClient(object):
    AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
    TOKEN_URL = "https://accounts.spotify.com/api/token"

    def __init__(self, client_id, secret_clientid, callback_uri, access_token = None):
        self.__callback_uri = callback_uri
        self.__clientid = client_id
        self.__secret_clientid = secret_clientid
        self.__callback_uri = callback_uri
        self.access_token = access_token
        self.__scope_query = None

    def define_scope(self, scope: str, *scopes):
        scope_query = '&scope=' + scope
        for scopeItem in scopes:
            scope_query += "+"
            scope_query += scopeItem
        self.__scope_query = scope_query

    def get_spotify_auth_page(self):
        if not self.__scope_query:
            scope = ["playlist-read-private", "playlist-read-collaborative",
                     "user-library-read", "user-follow-read", "user-top-read"]
            self.define_scope(*scope)

        authorization_redirect_url = self.AUTHORIZE_URL + '?response_type=code&client_id=' + \
            self.__clientid + '&redirect_uri=' + self.__callback_uri + self.__scope_query
        return authorization_redirect_url

    def request_access_token(self, authorization_code):
        data = {
            'grant_type': 'authorization_code',
            'code': authorization_code,
            'redirect_uri': self.__callback_uri
        }
        access_token_response = requests.post(
            self.TOKEN_URL, data=data, verify=False, allow_redirects=False,
            auth=(self.__clientid, self.__secret_clientid))
        tokens = json.loads(access_token_response.text)
        if access_token_response.status_code == 200:
            self.access_token = tokens['access_token']
        else:
            raise ConnectionRefusedError(access_token_response.text)


    def __create_header(self):
        return{'Authorization': 'Bearer ' + self.access_token}

    def call_get(self, url):
        return requests.get( url, headers=self.__create_header(), verify=False)

    def get_albums(self):
        api_call_response = self.call_get("https://api.spotify.com/v1/me/albums")
        return json.loads(api_call_response.text)