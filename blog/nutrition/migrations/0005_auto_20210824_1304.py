# Generated by Django 3.2.6 on 2021-08-24 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0004_remove_dish_ingredient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
