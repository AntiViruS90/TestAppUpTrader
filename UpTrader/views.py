from django.shortcuts import render, HttpResponse
from .models import *


def index(request):
    return render(request, 'index.html')


def index_firstname(request):
    database = User.objects.all()
    context = {'database': database}
    return render(request, 'index_firstname.html', context)


def index_lastname(request):
    database = User.objects.all()
    context = {'database': database}
    return render(request, 'index_lastname.html', context)


def index_email(request):
    database = User.objects.all()
    context = {'database': database}
    return render(request, 'index_email.html', context)


def index_phone_number(request):
    database = User.objects.all()
    context = {'database': database}
    return render(request, 'index_phone.html', context)