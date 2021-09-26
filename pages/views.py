import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {"title": "home"})
    # return HttpResponse("<h1>Welcome to Pages</h1>", content_type="text/html")


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {"title": "contact"})
    # return HttpResponse("<h1>Welcome to Pages</h1>", content_type="text/html")


def about_view(request, *args, **kwargs):
    ctx = {"title": "about",
           "my_text": "About Page",
           "my_number": 1123345,
           "my_list": (1, 2, 3, 4, 5, 6, 7, 8, 9, 0,),
           "html": "https://www.google.com/search?s=123"}

    return render(request, "about.html", ctx)
    # return HttpResponse("<h1>Welcome to Pages</h1>", content_type="text/html")


def developer_view(request, *args, **kwargs):
    return render(request, "developer.html", {"title": "developer"})
    # return HttpResponse("<h1>Welcome to Pages</h1>", content_type="text/html")
