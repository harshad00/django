from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello harshad in this page.")
    return render(render, 'index.html')

def about(request):
    # return HttpResponse("This is About page")
    return render(render, 'pages/about.html')

def contact(request):
    # return HttpResponse("This is my Contact page")
    return render(render, 'pages/contact.html')


