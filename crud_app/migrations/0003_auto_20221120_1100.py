# Generated by Django 3.1.4 on 2022-11-20 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
