# Generated by Django 2.1.5 on 2019-04-27 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addnews',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('matter', models.TextField(max_length=2000)),
            ],
        ),
    ]
