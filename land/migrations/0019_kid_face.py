# Generated by Django 2.0 on 2018-06-06 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0018_kid_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='kid',
            name='face',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d'),
        ),
    ]