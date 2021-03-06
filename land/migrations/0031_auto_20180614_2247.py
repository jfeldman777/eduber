# Generated by Django 2.0 on 2018-06-14 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('land', '0030_auto_20180613_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20)),
                ('letter', models.TextField(blank=True, max_length=250, null=True)),
                ('started', models.DateTimeField(auto_now_add=True)),
                ('person_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first', to=settings.AUTH_USER_MODEL)),
                ('person_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='second', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.TextField(blank=True, max_length=250, null=True)),
                ('written', models.DateTimeField(auto_now_add=True)),
                ('from_starter', models.BooleanField(default=False)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='land.Chat')),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='locations',
            field=models.ManyToManyField(to='land.Location'),
        ),
    ]
