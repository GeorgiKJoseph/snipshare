from django.shortcuts import render, get_object_or_404,redirect
from .models import Pastebin
from .forms import PastebinForm
from django.utils import timezone

def home(request):
    pastebin=Pastebin.objects.order_by('created_date')
    return render(request,'webapp/home.html',{'pastebin':pastebin})

def code_detail(request,pk):
    x=get_object_or_404(Pastebin,pk=pk)
    return render(request,'webapp/code_detail.html',{'x':x})


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