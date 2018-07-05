# Generated by Django 2.0 on 2018-07-03 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0043_chat_obj_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pref_addr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='land.Location'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pref_kid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='land.Kid'),
        ),
    ]