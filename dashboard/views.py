from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from dashboard.spotify_client import SpotifyClient

client_id = "<clientid>"
secret_clientid = "<secure_clientid>"
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
    print(access_code)
    spotify = SpotifyClient(client_id, secret_clientid, callback_uri)
    spotify.request_access_token(access_code)
    albums_response = spotify.get_albums()
    print(albums_response)
    return HttpResponse(albums_response.text)