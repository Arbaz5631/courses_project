from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('java/',views.java,name='java'),
    path('android/',views.android,name='android'),
    path('python/',views.python,name='python'),
    path('web/',views.web,name='web'),
    path('about/',views.about,name='about'),
    path('iCoder/',views.iCoder,name='iCoder'),
    path('privacyterms/',views.privacyterms,name='privacyterms'),
    path('contact/',views.contact,name='contact'),
    path('enquire/',views.enquire,name='enquire'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout')
]
