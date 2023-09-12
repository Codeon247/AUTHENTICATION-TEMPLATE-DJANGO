from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #autheticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "welcome, you have been logged in!!!")
            return redirect('index')
        else:
            messages.success(request, 'user not registered')
            return render(request, 'index.html', {})
    else:
        return render(request, 'index.html', {})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, 'you have been logged out')
    return redirect('index')