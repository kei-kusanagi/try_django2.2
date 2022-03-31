from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    my_title = "Rayquaza"
    context = {"title": my_title, "my_list": [1,2,3,4,5]}
    imagen = "https://pbs.twimg.com/media/EA1aIS9WsAA4QoR?format=jpg&name=large"
    # doc = "<h1>{title}</h1>".format(title=title)
    # django_render_doc = "<h1>{{title}}</h1>".format(title=title)
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {"title": "About us"})



def contact(request):
    return render(request, 'hello_world.html', {"title": "Contact us"})

    
def example_page(request):
    context = {"title": "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))

    
    