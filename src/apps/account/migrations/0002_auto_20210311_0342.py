# Generated by Django 3.1.5 on 2021-03-11 03:42

import apps.account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to=apps.account.models.profile_directory_photo),
        ),
    ]
