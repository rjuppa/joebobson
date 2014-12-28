from django.shortcuts import render
from django.conf.urls import patterns, url
from django.core.exceptions import *


def index(request):
    context = {'language_list': '', 'current_user': request.user, }
    return render(request, 'joeblog/joe_index.html', context)

def contact(request):
    context = {'language_list': '', 'current_user': request.user, }
    return render(request, 'joeblog/joe_contact.html', context)