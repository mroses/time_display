from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    context = {
        "datetime": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, 'time_display/index.html', context)

# Create your views here.
