from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from dashboard.spotify_client import SpotifyClient
from dashboard.application_properties import spotify_client_properties

client_id = spotify_client_properties["client_id"]
secret_clientid = spotify_client_properties["secret_clientid"]
callback_url = spotify_client_properties["callback_url"]

def index(request):
    if request.session.get('access_token'):
        return redirect('show_album')
    
    spotify = SpotifyClient(client_id, secret_clientid, callback_url)
    
    auth_url = spotify.get_spotify_auth_page()
    context = {
        'auth_url': auth_url,
    }
    return render(request, 'index.html', context)  

def logout(request):
    request.session['access_token'] = None
    return redirect('index')

def show_followed_artists(request):
    try:
        access_token = request.session.get('access_token')
        spotify = SpotifyClient(client_id, secret_clientid, callback_url, access_token)
        if not access_token:
            access_code = request.GET.get('code')
            spotify.request_access_token(access_code)
            request.session['access_token'] = spotify.access_token
        artist_items = spotify.get_artists()
        genre_set = spotify.get_genre_set(artist_items)
        context = {
            'artist_list': artist_items,
            'genre_set': genre_set,
        }
        return render(request, 'albums.html', context)
    except Exception as err:
         print("Exception while loading albums: {0}".format(err))
         return redirect('logout')