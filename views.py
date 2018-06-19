from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime

def index(request):
    context = {
        "datetime": strftime("%b, %d %Y %I:%H:%M %p %Z", localtime())
    }
    return render(request, 'time_display/index.html', context)

# Create your views here.
