# Generated by Django 4.2.5 on 2023-09-08 03:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finance', '0005_rename_stockowner_stockownermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockownermodel',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
