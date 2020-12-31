from django.db import models

# Create your models here.
class user(models.Model):
	name = models.CharField(max_length=128)
	password = models.CharField(max_length=64)
	email = models.CharField(max_length=128)
	
class verification(models.Model):
	token = models.CharField(max_length=32)
	