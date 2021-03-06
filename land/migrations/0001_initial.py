# Generated by Django 2.0 on 2018-05-31 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('date_of_birth', models.DateField(null=True)),
                ('face', models.ImageField(upload_to='uploads/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('otch', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='kid',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='land.Parent'),
        ),
    ]
