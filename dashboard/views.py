from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from dashboard.spotify_client import SpotifyClient
from dashboard.application_properties import spotify_client_properties
from dashboard.spotify_album_models import welcome_from_dict

client_id = spotify_client_properties["client_id"]
secret_clientid = spotify_client_properties["secret_clientid"]
callback_uri = "http://localhost:8080/dashboard/albums"

def index(request):
    spotify = SpotifyClient(client_id, secret_clientid, callback_uri)
    auth_url = spotify.get_spotify_auth_page()
    context = {
        'auth_url': auth_url,
    }
    return render(request, 'index.html', context)

def show_albums(request):   
    access_code = request.GET.get('code')
    spotify = SpotifyClient(client_id, secret_clientid, callback_uri)
    spotify.request_access_token(access_code)
    albums_response_dict = spotify.get_albums()

    result = welcome_from_dict(albums_response_dict)
    context = {
        'album_list': result.items,
    }
    return render(request, 'index.html', context)