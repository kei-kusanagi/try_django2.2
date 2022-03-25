from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, 'hello_world.html')


def about(request):
    return HttpResponse('<h1>About </h1>')


def contact(request):
    return HttpResponse('<h1>Contact</h1>')
    
    