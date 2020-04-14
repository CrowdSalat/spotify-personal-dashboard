from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    album_list = ["1","a","b"] 
    context = {
        'album_list': album_list,
    }
    return render(request, 'index.html', context)