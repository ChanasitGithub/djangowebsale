from django.shortcuts import render

# from django.http import HttpResponse  # Response website traffic
posts = [
    {
        "author": "Mr.I",
        "title": "Websale 1",
        "content": "First Sale Content",
        "date_post": "June 27, 2019",
    },
    {
        "author": "Chana",
        "title": "Websale 2",
        "content": "Second Sale Content",
        "date_post": "June 28, 2019",
    },
]


def home(request):
    # dic context
    context = {"posts": posts}
    return render(request, "websale/home.html", context)  # render return views


def about(request):
    return render(request, "websale/about.html", {"title": "About"})


def blog(request):
    return render(request, "websale/blog.html", {"title": "Blog"})



