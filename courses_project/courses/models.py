from django.db import models

# Create your models here.
class Contact(models.Model):

    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=70, default="")
    number = models.CharField(max_length=14, default="")
    desc = models.CharField(max_length=5000)

    def __str__(self):
        return self.name 


class Enquire(models.Model):

    enquire_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    enquire_email= models.CharField(max_length=70, default="")
    subject = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    number = models.CharField(max_length=14, default="")
    desc = models.CharField(max_length=5000)

    def __str__(self):
        return self.name 


