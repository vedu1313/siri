from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(req):
    return render (req,"html/home.html")

def index(req):
    return render(req,"html/index.html")

def aboutus(req):
    return render(req,"html/aboutus.html")

def service(req):
    return render(req,"html/service.html")


def contactus(req):
    return render(req,"html/contactus.html")
