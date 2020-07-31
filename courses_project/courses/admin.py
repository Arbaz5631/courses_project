from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Enquire)
admin.site.register(Contact)
admin.site.register(Course)
admin.site.register(Student)
