# Generated by Django 3.2.6 on 2021-08-24 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0003_dish_ingredient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='ingredient',
        ),
    ]
