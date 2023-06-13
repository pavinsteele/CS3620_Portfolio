from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobbies
from .models import Portfolio
# Create your views here.


def Home(request):
    return HttpResponse('Hey! My name is Pavin Steele and I am a senior at Weber State University!')


def hobbies(request):
    hobbies_list = Hobbies.objects.all()
    return HttpResponse(hobbies_list)


def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    return HttpResponse(portfolio_list)


def Contact(request):
    return HttpResponse('pavinsteele@mail.weber.edu')
