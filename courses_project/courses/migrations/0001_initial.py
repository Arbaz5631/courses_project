# Generated by Django 2.1.15 on 2020-07-20 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=14)),
                ('desc', models.CharField(max_length=5000)),
            ],
        ),
    ]