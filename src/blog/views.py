from re import template
from django.shortcuts import get_object_or_404, render
from django.http import Http404

# Create your views here.
from .models import BlogPost




def blog_post_list_view(request):
    # lista de objetos
    # puede ser una busqueda
    qs = BlogPost.objects.all() # SE MUESTRAN TODOS LOS BLOGS
    # qs = BlogPost.objects.filter(title__icontains='hola') ## SE MUESTRAN SOLO LOS QUE DIGAN 'hola'
    template_name = 'blog_post_list.html'
    context = {'object_list': qs }
    return render(request, template_name, context)


def blog_post_create_view(request):
    # crear objetos
    # ? usar form
    template_name = 'blog_post_create.html'
    context = {'form': None}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    # 1 objeto -> vista detallada
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_update.html'
    context = {"object": obj, 'form': None}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_delete.html'
    context = {"object": obj, 'form': None}
    return render(request, template_name, context)