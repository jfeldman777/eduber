# Generated by Django 2.0 on 2018-06-07 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0024_auto_20180606_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
            ],
        ),
    ]
