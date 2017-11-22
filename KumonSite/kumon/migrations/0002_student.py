# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kumon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=59)),
                ('nickname', models.CharField(max_length=25)),
                ('birthdate', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10)),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('phone_num', models.CharField(max_length=15)),
                ('tel_num', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('student_num', models.IntegerField()),
                ('school', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=50)),
                ('guardian_name', models.CharField(max_length=50)),
                ('relation', models.CharField(max_length=50)),
                ('guardian_num', models.CharField(max_length=30)),
                ('guardian_email', models.EmailField(blank=True, max_length=50)),
            ],
        ),
    ]
