from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
def home (request):
    return render(request, 'todoapp/todo.html',{})

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
    return render(request, 'todoapp/register.html',{})

def loginpage(request):
    return render(request, 'todoapp/login.html',{})
