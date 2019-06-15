from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm

# Create your views here.


def home_view(request):
    return render(request, 'index.html')


def add_view(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProfileForm()
    context = {
        'form': form
    }
    return render(request, 'add.html', context)


def list_view(request):
    profile = Profile.objects.all()
    return render(request, 'list.html', {'profiles': profile})

