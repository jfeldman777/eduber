# Generated by Django 2.0 on 2018-06-22 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0040_auto_20180621_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='prop',
            name='age',
            field=models.PositiveIntegerField(blank=True, default=10, null=True),
        ),
    ]