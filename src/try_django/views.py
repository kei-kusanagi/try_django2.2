from django.http import HttpResponse



def home_page(request):
    return HttpResponse('<h1>Hola Mundo</h1>')


def about(request):
    return HttpResponse('<h1>About </h1>')


def contact(request):
    return HttpResponse('<h1>Contact</h1>')
    
    