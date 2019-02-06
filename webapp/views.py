from django.shortcuts import render, get_object_or_404,redirect
from .models import Pastebin, UserAccount, Vote, Friend
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
    pastebin=Pastebin.objects.order_by('-created_date').filter(author=request.user)
    try:
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
        for f in friends:
                temp=Pastebin.objects.filter(author=f.username)
                pastebin = pastebin | temp
    except Friend.DoesNotExist:
        friends=None
    return render(request,'webapp/home.html',{'pastebin':pastebin})


@login_required
def change_vote_status(request,pastebin_pk):
    pastebin=Pastebin.objects.get(pk=pastebin_pk)
    try: 
        voters = Vote.objects.get(current_pastebin=pastebin)
        users = voters.users.all()
    except Vote.DoesNotExist:
        users=None

    if users == None:
        Vote.upvote(pastebin,request.user)
    elif request.user in users:
        Vote.downvote(pastebin,request.user)

    else:
        Vote.upvote(pastebin,request.user)
    y=len(users)
    pastebin.upvotes=y
    pastebin.save()
     
#    x=get_object_or_404(Pastebin,pk=pastebin_pk)
#    return render(request,'webapp/code_detail.html',{'x':x})
    return redirect('code_detail', pk = pastebin_pk)



@login_required
def code_detail(request,pk):
    x=get_object_or_404(Pastebin,pk=pk)
    pastebin=Pastebin.objects.get(pk=pk)
    try: 
        voters = Vote.objects.get(current_pastebin=pastebin)
        users = voters.users.all()
    except Vote.DoesNotExist:
        users=None
    if users == None:
        check = 'False'
    elif request.user in users:
        check = 'True'
    else:
        check = 'False'                                  #here check is used to decide the button (like/dislike)
    return render(request,'webapp/code_detail.html',{'x':x,'check':check})


@login_required
def view_profile(request, pk=None):   #this view can be call from friends.html to view friend's profile(no done yet)
        if pk:
                users=User.objects.get(pk=pk)
                return render(request,'webapp/friends_profile.html',{'users':users})
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
def change_friends(request,operation,pk):
        new_friend = User.objects.get(pk=pk)
        if operation == 'make':
                Friend.make_friend(request.user,new_friend)
                return redirect('view_others')
        elif operation == 'lose':      
                Friend.lose_friend(request.user,new_friend)
                return redirect('view_friends')
        return redirect('home')


@login_required
def view_others(request):
        users = User.objects.exclude(id=request.user.id)
        new_friend = User.objects.get(pk=request.user.pk)
        Friend.make_friend(request.user,request.user)
        try: 
                friend = Friend.objects.get(current_user=request.user)
                friends = friend.users.all() 
        except Friend.DoesNotExist:
                friends=None                       
        return render(request,'webapp/others.html',{'users':users,'friends':friends})


@login_required
def view_friends(request):
        try:                
                friend = Friend.objects.get(current_user=request.user)
                friends = friend.users.all()
        except Friend.DoesNotExist:
                friends=None
        args = {'friends':friends}
        return render(request,'webapp/friends.html',args)
