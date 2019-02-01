from django.shortcuts import render, get_object_or_404,redirect
from .models import Pastebin, Account, Vote
from .forms import PastebinForm, AccountForm, LoginForm
from django.utils import timezone

def home(request):
    pastebin=Pastebin.objects.order_by('created_date')
    return render(request,'webapp/home.html',{'pastebin':pastebin})

def code_detail(request,pk):
    x=get_object_or_404(Pastebin,pk=pk)
    return render(request,'webapp/code_detail.html',{'x':x})

def signup(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')         #has to be changed to login page or home page
    else:
        form = AccountForm()
    return render(request,'webapp/signup.html',{'form':form})

def login(request):                         #to be modified
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('home')         #has to be changed to login page or home page
    else:
        form = LoginForm()
    return render(request,'webapp/login.html',{'form':form})


def add_new(request):
    if request.method == "POST":
        form = PastebinForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = timezone.now()
            post.save()
            return redirect('code_detail', pk=post.pk)
    else:
        form = PastebinForm()
    return render(request,'webapp/add_new.html',{'form':form})
