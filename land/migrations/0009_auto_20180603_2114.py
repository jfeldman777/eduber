# Generated by Django 2.0 on 2018-06-03 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0008_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ask_parent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='ask_producer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='ask_teacher',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='has_parent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='has_producer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='has_teacher',
            field=models.BooleanField(default=False),
        ),
    ]
