from re import template
from django.shortcuts import get_object_or_404, render
from django.http import Http404

# Create your views here.
from .models import BlogPost

# GET -> 1 object
# FILTER -> [] objects

def blog_post_detail_page(request, slug):
    print("DJANGO DICE", request.method, request.path, request.user)
    queryset = BlogPost.objects.filter(slug=slug)
    if queryset.count() == 0:
        raise Http404
    obj = queryset.first()
    # # obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_detail.html'
    context = {"object": obj} # {"title": obj.title}
    return render(request, template_name, context)