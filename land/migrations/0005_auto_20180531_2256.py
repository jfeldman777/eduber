# Generated by Django 2.0 on 2018-05-31 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0004_auto_20180531_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kid',
            name='face',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d'),
        ),
    ]
