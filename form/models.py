# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	image = models.ImageField(blank = True)
	name = models.CharField(max_length=30)
	username = models.CharField(max_length=30,primary_key=True)
	desig = models.CharField(max_length=25)
	skills = models.Charfield(max_length=50)
	edu = models.Charfield(max_length=30)
	about = models.CharField(max_length=100)
	locations = models.Charfield(max_length=30)
