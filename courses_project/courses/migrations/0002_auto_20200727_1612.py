# Generated by Django 3.0.8 on 2020-07-27 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='name',
            new_name='student',
        ),
    ]
