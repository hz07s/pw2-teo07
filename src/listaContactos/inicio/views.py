from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})

def anotherView(*args, **kwargs):
    return HttpResponse('<h1>Sólo es otra página</h1>')