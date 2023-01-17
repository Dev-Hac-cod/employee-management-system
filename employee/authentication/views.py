import email
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate ,login

# Create your views here.
def home(request):
    return render(request,"authentication/home.html")

def signup(request):
    if request.method == "POST":
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['pass1']
        pass2 = request.POST['pass2']
        if User.objects.filter(username=username):
            messages.warning(request,'Username is alrady exits')
            return redirect('signup')
        else: 
            myuser = User.objects.create_user(username,email,password)
            myuser.save()
            messages.warning(request, "Your Account has been successfully created.")
            return redirect('home')
    return render(request, "authentication/signup.html")


def signin(request):
    if request.method == "POST":
        username=request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username,password=pass1)

        if user is not None:
            login(request, user)
            return redirect('employee_insert')

        else:
            messages.error(request, ' Password or UserId Incorrect!!')
            return redirect('signin')
    return render(request, "authentication/signin.html") 