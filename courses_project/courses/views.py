from django.shortcuts import render,redirect
from . models import Contact,Enquire
from django.contrib import messages
from .forms import  CreateUserForm
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib.auth.models import Group
from courses.models import *

# Create your views here.


def login(request):
    if request.method == 'POST':
       username = request.POST.get("username")
       password = request.POST.get("password")
       user = authenticate(request, username=username, password=password)
       if user is not None:
           dj_login(request,user)
           print('hello1')
           return redirect('/')
       else:
           p
           messages.info(request,'Your Password is Incorrect')
           return redirect('login')
    
    param={}
    return render(request, 'courses/login.html',param)

def logout(request):
    dj_logout(request)
    return redirect('login')
    

def register(request):
     form = CreateUserForm()
     if request.method=='POST':
         form= CreateUserForm(request.POST)
         if form.is_valid():
             user=form.save()
             username=form.cleaned_data.get('username')
             group=Group.objects.get(name='Student') #
             user.groups.add(group)# both hash tag line are used when user register in the page then then itself add the customer group.
             
             
             
             messages.success(request,'Accout was created for ' +username)
             return redirect('/login')
     
     param={'form':form}
     return render(request, 'courses/register.html',param)

def index(request):
    usercourses = request.user.username
    student = Student.course_set
    return render(request, 'courses/index.html')


def java(request):
    return render(request, 'courses/java.html')


def python(request):
    return render(request, 'courses/python.html')


def android(request):
    return render(request, 'courses/android.html')


def web(request):
    return render(request, 'courses/web.html')


def about(request):
    return render(request, 'courses/about.html')


def iCoder(request):
    return render(request, 'courses/iCoder.html')


def privacyterms(request):
    return render(request, 'courses/privacyterms.html')


def contact(request):
        if request.method == "POST":
           name = request.POST.get('name', '')
           email = request.POST.get('email', '')
           number = request.POST.get('number', '')
           desc = request.POST.get('desc', '')
           con1 = Contact(name=name, email=email, number=number, desc=desc)
           con1.save()

        return render(request,'courses/contact.html')


def enquire(request):
    if request.method == "POST":
           name = request.POST.get('name', '')
           email2 = request.POST.get('email2', '')
           subject= request.POST.get('subject', '')
           dob= request.POST.get('dob', '')
           state= request.POST.get('state', '')
           number = request.POST.get('number', '')
           desc = request.POST.get('desc', '')
           con2 = Enquire(name=name, enquire_email=email2,subject=subject,dob=dob,state=state,number=number, desc=desc)
           con2.save()
    return render(request, 'courses/enquire.html')
