from django.shortcuts import render, get_object_or_404
from .models import Pastebin

def home(request):
    pastebin=Pastebin.objects.order_by('created_date')
    return render(request,'webapp/home.html',{'pastebin':pastebin})

def code_detail(request,pk):
    x=get_object_or_404(Pastebin,pk=pk)
    return render(request,'webapp/code_detail.html',{'x':x})