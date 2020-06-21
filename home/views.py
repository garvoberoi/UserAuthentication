from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

# id-garv pass- Mynote230 for test user
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginuser(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('pass') 
        user = authenticate(username=name, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")