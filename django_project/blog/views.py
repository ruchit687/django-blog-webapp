# Note: by default django looks for the template subdirectory and installed apps
# blog_app -> template -> blog-template -> .html files for blog app
# there are many ways to load a template, one way is to load the template & then render it & pass that to our
# httpResponse but this is longer way... So django provides us with a shortcut method to do the same -> render method.

from django.shortcuts import render
from django.http import HttpResponse

# dummy data, creating fake post list of dictionary, each dict - info associated with a post.
posts = [
    {
        'author': 'RuchitPorwal',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'September 29, 2019'
    },
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 'September 30, 2019'
    }
]


def home(request):
    context = {
        'posts': posts  # list of dictionary containing posts
        # will let us pass the data to template & let it access within the template
        # so whatever key name is mentioned would be accessible from the template.
    }
    return render(request, 'blog/home.html', context=context)
    # context passing info into our template
    # >>> return HttpResponse('<h1>Blog Home</h1>')  <<<
    # we can send complete html structure here
    # but that will be messy,
    # so we create template (by default django looks fro a template sub directory & each of our installed apps)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
    # return HttpResponse('<h1>Blog About</h1>')
