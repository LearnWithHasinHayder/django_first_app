from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def say_hello(request):
    return HttpResponse("Hello, Django!")


# def homepage(request):
#     return HttpResponse('HomePage Content')


def homepage(request):
    page = {"title": "Home page!!! Awesomeeeeeeee", "content": "Welcome to the home page"}
    return render(request, "index.html", page)


def about(request):
    return render(request, "about.html")


def contact(request):
    email = "contact@example.com"
    social_profiles = [
        "Facebook: fb.me/example",
        "Twitter: twitter.com/example",
        "Instagram: instagram.com/example",
        "Youtube : youtube.com/channelid"
    ]
    hq="x"
    return render(request, "contact.html", {"emailaddress": email, "socialprofiles":social_profiles, "hq":hq})

def experiment(request, person=None):
    if person is None:
        person = "Guest"
    return render(request, "experiment.html", {"data":person})

def experiment_greet(request, person, greet):
    return render(request, "experiment.html", {"data":person, "greetings":greet})