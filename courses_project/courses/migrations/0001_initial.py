# Generated by Django 3.0.8 on 2020-07-26 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(default='', max_length=70)),
                ('number', models.CharField(default='', max_length=14)),
                ('desc', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Enquire',
            fields=[
                ('enquire_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('enquire_email', models.CharField(default='', max_length=70)),
                ('subject', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('number', models.CharField(default='', max_length=14)),
                ('desc', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(max_length=20)),
                ('faculty_name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Web_development', 'Web_development'), ('Android', 'Android'), ('Python', 'Python'), ('Java', 'Java'), ('C', 'C'), ('Perl', 'Perl'), ('Ruby', 'Ruby'), ('Html', 'Html'), ('CSS', 'CSS'), ('Bootstrap', 'Bootstrap'), ('Django', 'Django'), ('Angular', 'Angular'), ('Node.js', 'Node.js'), ('React', 'React'), ('C#', 'C#'), ('C++', 'C++')], max_length=200, null=True)),
                ('price', models.IntegerField(default='0')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='courses.Student')),
            ],
        ),
    ]
