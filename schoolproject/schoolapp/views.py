from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages,auth
from django.shortcuts import render
from django.contrib.auth import  authenticate


def demo(request):
    return render(request,"index.html")

def login(request):
    if request.method == "POST":
       username = request.POST['username']
       password = request.POST['password']
       user=auth.authenticate(username=username,password=password)
       if user is not None:
          auth.login(request,user)
          return redirect('/')
       else:
          messages.info(request,"invalid")
          return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if   User.objects.filter(username=username).exists():
                 messages.info(request,"username taken")
                 return redirect('register')


            else:
                  user = User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password)
                  user.save();


        else:
                  messages.info(request,"password not matching")
                  return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


def new(request):
    return render(request,"new.html")


def form(request):
    return render(request,"form.html")
