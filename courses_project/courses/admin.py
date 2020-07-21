from django.contrib import admin

# Register your models here.
from .models import Enquire,Contact
admin.site.register(Enquire)
admin.site.register(Contact)
