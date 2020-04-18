from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from dashboard.spotify_client import SpotifyClient
from dashboard.application_properties import spotify_client_properties

client_id = spotify_client_properties["client_id"]
secret_clientid = spotify_client_properties["secret_clientid"]
callback_uri = "http://localhost:8080/dashboard"

def index(request):
    access_code = request.GET.get('code')
    spotify = SpotifyClient(client_id, secret_clientid, callback_uri)

    if not access_code:
        auth_url = spotify.get_spotify_auth_page()
        context = {
            'auth_url': auth_url,
        }
    else:
        spotify.request_access_token(access_code)
        print("-------" + str(spotify.access_token) + "--------_")
        request.session['access_token'] = spotify.access_token
        context = {
            'auth_url': None,
        }
    return render(request, 'index.html', context)  

def show_followed_artists(request):
    access_code = request.session.get('access_token')
    spotify = SpotifyClient(client_id, secret_clientid, callback_uri, access_code)
    artist_items = spotify.get_artists()
    context = {
        'artist_list': artist_items,
    }
    return render(request, 'index.html', context)