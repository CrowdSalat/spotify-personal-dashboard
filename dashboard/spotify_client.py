from typing import *
import requests
import json
import subprocess
import sys
import dashboard.spotify_artist_models

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
        resp = requests.get( url, headers=self.__create_header(), verify=False)
        return json.loads(resp.text)

    def get_artists(self):
        try:
            resp_json = self.call_get("https://api.spotify.com/v1/me/following?type=artist")
            resp_obj = dashboard.spotify_artist_models.welcome_from_dict(resp_json)
            next_page = resp_obj.artists.next
            while next_page:
                resp_json2 = self.call_get(next_page)
                resp_ob2 = dashboard.spotify_artist_models.welcome_from_dict(resp_json2)
                resp_obj.artists.items.extend(resp_ob2.artists.items)
                next_page = resp_ob2.artists.next

            return resp_obj.artists.items
        except AssertionError:
            print("Exception at: " + str(next_page))

    def get_genre_set(self, artist_items: List[dashboard.spotify_artist_models.Item]) -> Set[str]:
        genre_set  = set()
        for artist in artist_items:
            genre_set.update(artist.genres)
        return genre_set