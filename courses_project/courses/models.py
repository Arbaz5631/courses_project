from django.db import models
from django.contrib.auth.models import User


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

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) # With the help of this login user can only see herself products.
    name = models.CharField(max_length=200 , null=True)
    phone = models.CharField(max_length=200 , null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic=models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name



class Course(models.Model):
    CATEGORY=(('Web_development','Web_development'),
            ('Android','Android'),
            ('Python','Python'),
            ('Java','Java'),
            ('C','C'),
            ('Perl','Perl'),
            ('Ruby','Ruby'),
            ('Html','Html'),
            ('CSS','CSS'),
            ('Bootstrap','Bootstrap'),
            ('Django','Django'),
            ('Angular','Angular'),
            ('Node.js','Node.js'),
            ('React','React'),
            ('C#','C#'),
            ('C++','C++'),
              )
    student=models.ForeignKey(Student,max_length=200, on_delete=models.CASCADE)
    duration=models.CharField(max_length=20)
    faculty_name=models.CharField(max_length=200)
    category=models.CharField(null=True, max_length=200, choices=CATEGORY)
    price=models.IntegerField(default="0")
    image=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.category









