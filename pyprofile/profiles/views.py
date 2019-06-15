from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile

# Create your views here.


def index(request):
    profile = Profile.objects.all()
    return render(request, 'index.html', {'profile': profile})


def home_view(request):
    return HttpResponse('<h1>home view</h1>')

