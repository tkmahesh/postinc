# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-13 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('image', models.ImageField(blank=True, upload_to=b'')),
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('desig', models.CharField(max_length=25)),
                ('skills', models.CharField(max_length=50)),
                ('edu', models.CharField(max_length=30)),
                ('about', models.CharField(max_length=100)),
                ('locations', models.CharField(max_length=30)),
            ],
        ),
    ]
