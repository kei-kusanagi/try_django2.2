from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    my_title = "Rayquaza"
    imagen = "https://pbs.twimg.com/media/EA1aIS9WsAA4QoR?format=jpg&name=large"
    # doc = "<h1>{title}</h1>".format(title=title)
    # django_render_doc = "<h1>{{title}}</h1>".format(title=title)
    return render(request, 'hello_world.html', {"title": my_title, "imagen": imagen})


def about(request):
    return render(request, 'about.html', {"title": "About us"})



def contact(request):
    return render(request, 'hello_world.html', {"title": "Contact us"})

    
def example_page(request):
    context = {"title": "Example"}
    algo_aqui = "hello_world.html"
    return HttpResponse(algo_aqui)

    
    