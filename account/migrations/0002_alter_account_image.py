# Generated by Django 4.2.1 on 2023-05-25 10:51

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=account.models.image_path),
        ),
    ]