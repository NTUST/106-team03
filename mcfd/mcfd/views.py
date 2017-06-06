from django.shortcuts import HttpResponseRedirect,render
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request,'index.html')

