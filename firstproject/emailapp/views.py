from django import http
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import *
# Create your views here.
def mail(request):
    subject="greetings"
    msg="congrats on ur registration"
    to="nibingunnerzz1111@gmail.com"
    res=send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
    if res==1:
        m="Mail success"
    else:
        m='mailing failed'
    return HttpResponse(m)        
def flup(request):
    if request.method=='GET':
         context={}
         context['form']=Filesup()
         return render(request,'fileup.html',context)
    elif request.method=='POST':
        fp=Filesup(request.POST,request.FILES)
        if fp.is_valid():
            fil=request.FILES['file']
            handle_method(fil)
            return HttpResponse('fileuploaded')
def handle_method(f):
    with open('emailapp\\static\\upload\\'+f.name,'wb+') as dest:
        for c in f.chunks():
            dest.write(c)
    
        
   