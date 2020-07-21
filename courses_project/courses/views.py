from django.shortcuts import render
from . models import Contact,Enquire
# Create your views here.


def index(request):
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
