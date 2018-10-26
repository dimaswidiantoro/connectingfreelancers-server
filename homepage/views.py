from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.


def homepage(request):
    return render(request,'homepage/homepage.html')
