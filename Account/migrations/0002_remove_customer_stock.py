# Generated by Django 4.2.5 on 2023-09-08 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='stock',
        ),
    ]
