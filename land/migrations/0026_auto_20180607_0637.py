# Generated by Django 2.0 on 2018-06-07 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0025_subject'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]