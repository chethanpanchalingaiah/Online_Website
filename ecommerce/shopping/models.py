from django.db import models



class Customer(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=15)
	choices = (("M","Male"),("F","Female"))
	sex = models.CharField(max_length=1, choices=choices)

# Create your models here.
