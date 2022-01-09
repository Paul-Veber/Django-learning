from django.shortcuts import render

# Create your views here.

def hello(request, username):
    return render(request, 'index.html', {"username":username})

