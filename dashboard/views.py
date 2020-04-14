from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):

    album_list = ["1","a","b"] 
    template = loader.get_template('index.html')
    context = {
        'album_list': album_list,
    }

    return HttpResponse(template.render(context, request))