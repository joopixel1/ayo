# blog/models.py
from django.db import models
from phone_field import PhoneField
from django.urls import reverse


# Create your models here.
class Service(models.Model):
	title = models.CharField(max_length=200)
	message = models.TextField()

	def __str__(self):
		return self.title




class People(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	phone_no = PhoneField(help_text='Mobile phone number')
	email = models.EmailField(help_text='email address')

	def __str__(self):
		return self.first_name + " " + self.last_name
		
	def get_absolute_url(self): # new
		return reverse('thanks')



class Languages(models.Model):
	title = models.CharField(max_length=200)

	def __str__(self):
		return self.title

