# Generated by Django 4.2.5 on 2023-09-08 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scraper', '0002_scrapermodel_name_scrapermodel_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapermodel',
            name='can_work',
            field=models.BooleanField(default=False),
        ),
    ]
