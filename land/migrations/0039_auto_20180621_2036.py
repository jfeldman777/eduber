# Generated by Django 2.0 on 2018-06-21 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0038_auto_20180621_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prop',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='land.Subject'),
        ),
    ]