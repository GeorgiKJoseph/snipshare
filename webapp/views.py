from django.shortcuts import render, get_object_or_404,redirect
from .models import Pastebin, UserAccount, Vote
from .forms import PastebinForm, AccountForm, LoginForm, EditProfileForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method=='POST':
        form= AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    
    else:
        form= AccountForm()
        return render(request, 'webapp/signup.html',{'form':form})

    
@login_required
def home(request):
    pastebin=Pastebin.objects.order_by('created_date').filter(author=request.user)
    return render(request,'webapp/home.html',{'pastebin':pastebin})


@login_required
def code_detail(request,pk):
    x=get_object_or_404(Pastebin,pk=pk)
    return render(request,'webapp/code_detail.html',{'x':x})


@login_required
def view_profile(request, pk=None):

        if pk:
                users=User.objects.get(pk=pk)
        else:
                users=request.user

        return render(request,'webapp/profile.html',{'users': users})



@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return render(request,'webapp/profile.html',{})
    
    else: 
        form = EditProfileForm(instance=request.user)
        return render(request,'webapp/edit_profile.html',{'form':form})


@login_required
def add_new(request):
    if request.method == 'POST':
        form = PastebinForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('code_detail', pk=post.pk)
    else:
        form = PastebinForm()
        return render(request,'webapp/add_new.html',{'form':form})

@login_required
def view_friends(request):
        users = User.objects.all()
        return render(request,'webapp/friends.html',{'users':users})
