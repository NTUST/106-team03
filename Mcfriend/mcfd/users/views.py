from django.shortcuts import render,HttpResponseRedirect
from django.contrib import auth
from .forms import CustomUserChangeForm, CustomUserCreationForm
def login(request):
    if request.user.is_authenticated(): 
        return HttpResponseRedirect('/')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        return render(request,'registration/login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = CustomUserCreationForm()
    context = {'form':form}
    return render(request,'registration/register.html',context)
