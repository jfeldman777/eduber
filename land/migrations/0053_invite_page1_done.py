# Generated by Django 2.0 on 2018-07-30 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0052_event_page1'),
    ]

    operations = [
        migrations.AddField(
            model_name='invite',
            name='page1_done',
            field=models.BooleanField(default=False),
        ),
    ]