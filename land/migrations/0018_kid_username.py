# Generated by Django 2.0 on 2018-06-06 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0017_auto_20180606_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='kid',
            name='username',
            field=models.SlugField(default='1', max_length=15),
        ),
    ]
