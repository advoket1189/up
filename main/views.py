from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from  django.contrib import  messages
#from .forms import CustomUserCreationForm

# Create your views here.

def home(request):
    title = 'Home'
    context = {'title': title,}
    templates = 'home.html'
    return render(request, templates, context, title)


def about(request):
    title = 'About'
    context = {'title': title,}
    templates = 'about.html'
    return render( request, templates, context, title)

def how_it_works(request):
    title = 'How it works'
    context = {'title': title,}
    templates = 'works.html'
    return render( request, templates, context, title)


def service(request):
    title = 'Service'
    context = {'title': title,}
    templates = 'service.html'
    return render(request, templates, context,)

def contact(request):
    title = 'Contact'
    context = {'title': title,}
    templates = 'contact.html'
    return render(request, templates, context,)







