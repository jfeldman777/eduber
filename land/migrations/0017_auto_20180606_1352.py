# Generated by Django 2.0 on 2018-06-06 10:52

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('land', '0016_auto_20180605_2348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('birth_date', models.DateField()),
                ('locations', django.contrib.postgres.fields.ArrayField(base_field=models.SlugField(blank=True), blank=True, null=True, size=5)),
                ('letter', models.TextField(blank=True, max_length=250, null=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='web',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]