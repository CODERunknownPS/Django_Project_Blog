from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from .models import my_blog
from .forms import Edit_Blog


def index(request):

    blogs = my_blog.objects.all()
    context = {'blogs': blogs}
    return render(request,'home.html',context)


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def user_login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request,'Login Failed')
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        fname = request.POST.get('Fname')
        lname = request.POST.get('Lname')
        uname = request.POST.get('Uname')
        email = request.POST.get('Email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1!=pass2:
            messages.warning(request,'Password does not match')
            return redirect('register')
        elif User.objects.filter(username=uname).exists():
            messages.warning(request,'Username Already Exists')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.warning(request,'Email Already Exists')
            return redirect('register')
        else:
            user = User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=pass1)
            user.save()
            messages.success(request,'User has been registred successfully ')
            return redirect('login')
        
    return render(request,'register.html')

def user_logout(request):
    logout(request)
    return redirect('/')


def post_blog(request):

    if request.method=="POST":
        
        title = request.POST.get('title')
        sub_title = request.POST.get('sub_title')
        desc = request.POST.get('Description')
        blogs = my_blog(title=title, dsc = desc, sub_title=sub_title)
        blogs.save()

        messages.success(request,'Post Added successfully ')
        return redirect('/')

    return render(request,'post_blog.html')

def post(request,id):

    blog = my_blog.objects.get(id = id)
    context = {'blog': blog}
    return render(request,'post.html',context)

def delete(request,id):

    blog = my_blog.objects.get(id = id)
    blog.delete()
    messages.success(request,'Post Deleted successfully ')
    return redirect('/')


def edit(request,id):

    blog = my_blog.objects.get(id = id)
    editblog = Edit_Blog(instance=blog)
    if request.method=='POST':
        form = Edit_Blog(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request,'Post has been Updated successfully ')
            return redirect('/')

    return render(request,'edit_blog.html',{'edit_blog':editblog})
    

