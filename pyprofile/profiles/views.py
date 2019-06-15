from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile

# Create your views here.


def home_view(request):
    return render(request, 'index.html')


def add_view(request):
    return HttpResponse('<h1>Add view</h1>')


def list_view(request):
    profile = Profile.objects.all()
    return render(request, 'list.html', {'profiles': profile})

