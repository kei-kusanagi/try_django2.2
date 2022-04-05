from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm

def home_page(request):
    my_title = "Rayquaza"
    imagen = "https://pbs.twimg.com/media/EA1aIS9WsAA4QoR?format=jpg&name=large"
    context = {"title": my_title}
    if request.user.is_authenticated:
        context = {"title": my_title, "my_list": [1,2,3,4,5], "imagen": imagen}
    
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {"title": "About us"})



def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context =  {
        "title": "Contact us", 
        "form": form
    }
    return render(request, 'form.html', context)

    
def example_page(request):
    context = {"title": "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))

    
    