# Generated by Django 2.0 on 2018-06-03 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0006_auto_20180601_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kid',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Kid',
        ),
        migrations.DeleteModel(
            name='Parent',
        ),
    ]
