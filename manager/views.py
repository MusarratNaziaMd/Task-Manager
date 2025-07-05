from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import manager
from django.contrib.auth.decorators import login_required

def registerpage(request):
    if request.method=="POST":
        username=request.POST.get('name')
        password=request.POST.get('password')
        confirm=request.POST.get('confirm')
        if password!=confirm:
            return render(request,'register.html',{'result':'Password doesnot match!'})
        if User.objects.filter(username=username).exists():
            return render(request,'register.html',{'result':'User already exists!'})
        User.objects.create_user(username=username , password=password)
        return redirect('login')
    return render(request,'register.html')


def loginpage(request):
     if request.method=="POST":
        username=request.POST.get('name')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if not User.objects.filter(username=username).exists():
            return redirect('register')  # redirect to register if user doesn't exist

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'result': 'Invalid password!'})
        
     return render(request,'login.html')    


def homepage(request):
    if request.method=="POST":
        title=request.POST.get('title')
        if title:
            manager.objects.create(user=request.user,title=title)
    task=manager.objects.filter(user=request.user)
    return render(request,'home.html',{'manager':task})

# Mark Task as Completed
@login_required(login_url='login')
def complete_task(request, id):
    task = manager.objects.get(id=id, user=request.user)
    task.completed = True
    task.save()
    return redirect('home')


# Delete Task
@login_required(login_url='login')
def delete_task(request, id):
    task = manager.objects.get(id=id, user=request.user)
    task.delete()
    return redirect('home')

def logoutpage(request):
    logout(request)
    return render(request,'logout.html')



# Create your views here.
