# Note: by default django looks for the template subdirectory and installed apps
# blog_app -> template -> blog-template -> .html files for blog app
# there are many ways to load a template, one way is to load the template & then render it & pass that to our
# httpResponse but this is longer way... So django provides us with a shortcut method to do the same -> render method.

from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
    # context passing info into our template
    # >>> return HttpResponse('<h1>Blog Home</h1>')  <<<
    # we can send complete html structure here
    # but that will be messy,
    # so we create template (by default django looks fro a template sub directory & each of our installed apps)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
    # return HttpResponse('<h1>Blog About</h1>')
