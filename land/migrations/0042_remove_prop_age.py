# Generated by Django 2.0 on 2018-06-22 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0041_prop_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prop',
            name='age',
        ),
    ]
