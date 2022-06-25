import imp
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import studentform,Bookform,regform
from .models import Students
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
def home(request):
        request.session['user']='Rahul'
        return render(request,'home.html')
def setcookie(request):
    res=HttpResponse('cookie set')
    res.set_cookie('Quest','Pythonintersnhip')
    return res
def getcookie(request):
    t=request.COOKIES['Quest']
    return HttpResponse('COOKIEname:'+t)     
def forms(request):
    student=studentform()
    a=['apple','banana','orange']
    return render(request,'studentform.html',{'formview':student,'listvar':a})
def modelform(request):
    if request.method=='GET':
         mform=Bookform()
         dct={}
         dct['mfor']=mform
         return render(request,'mform.html',dct)
    elif request.method=='POST':
        b=Bookform(request.POST)
        print(b)
        if b.is_valid():
            b.save()
        return render(request,'mform.html')
def form3(request):
    if request.method=='GET':
         return render(request,'thirdform.html')
    elif request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        email=request.POST['email']
        phone=request.POST['phone'] 
        a=Students.objects.create(name=name,age=age,phone=phone,email=email,address=address)
        return redirect('form3')
def viewdata(request):
    a=Students.objects.all
    context={}
    context['data']=a
    context['uu']=request.session['user']
    return render(request,'viewdata.html',context)
def deletstud(request,uid):
    request.session['suid']=uid
    #sessionbuilding
    a=Students.objects.filter(id=uid).delete()
    return redirect('view')
def updatestud(request,uid):
    if request.method=='GET':
        a=Students.objects.get(id=uid)
        context={}
        context['sdata']=a
        return render(request,'editdata.html',context)
    elif request.method=='POST':
         name=request.POST['name']
         age=request.POST['age']
         address=request.POST['address']
         email=request.POST['email']
         phone=request.POST['phone'] 
         obk=Students.objects.filter(~Q(age=20)) #used for not equal to 20
         obk=Students.objects.filter(Q(age=20)&Q(name='Nibin')) #and operator
         obk=Students.objects.filter(Q(age=20)|Q(name='Nibin')) #or operator
         ob=Students.objects.filter(id=uid).update(name=name,age=age,phone=phone,email=email,address=address)
         return redirect('view')
def userreg(request):
    if request.method=='GET':
         context={}
         context['form']=regform()
         return render(request,'userreg.html',context)
    elif request.method=='POST':
        form=regform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('h')
   
def userreg2(request):
    if request.method=='GET':
         return render(request,'reg1form.html')
    else:
        uname=request.POST['user']
        p1=request.POST['pass1']
        p2=request.POST['pass2']
        if p1==p2:
            a=User.objects.create_user(username=uname,password=p1)
            return redirect('h') 

def log(request):
    if request.method=='GET':
        context={}
        context['form']=AuthenticationForm()
        return render(request,'login.html',context)
    elif request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.cleaned_data.get('username')
            pwd=form.cleaned_data.get('password')
            user=authenticate(request,username=user,password=pwd)
            if user:
                login(request,user)
                return redirect('h')
            else:
                print(form.errors)
                return redirect('log')
                    
    