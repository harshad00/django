from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Hello my firends this is my add')
    return render(request, 'index.html')

def h(request):
    # return HttpResponse('Hello my firends this is my add')
    return render(request, 'pages/h.html')

