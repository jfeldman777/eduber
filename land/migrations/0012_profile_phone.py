# Generated by Django 2.0 on 2018-06-04 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0011_auto_20180603_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]