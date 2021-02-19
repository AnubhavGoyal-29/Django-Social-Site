from django.http import HttpResponse
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

def home_view(request):
    user = request.user
    if user.is_authenticated:
        hello = 'Hello world'

        context = {
            'user': user,
            'hello' : hello,
        }
        return render(request, 'main/home.html', context)
    else:
        return redirect('/login/')
    # return HttpResponse('Hello world')
def login_view(request):
    if request.method=='POST':
        username=request.POST['user']
        password=request.POST['pass']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            print(user)
            login(request,user)
            return redirect('/posts/')
    return render(request,'login.html',{})
def register_view(request):
    if request.method=='POST':
        username=request.POST['user']
        password=request.POST['pass']
        user = User.objects.create_user(username,password)
        user.save()
        login(request,user)
        return redirect('/posts/')
    return render(request,'register.html',{})