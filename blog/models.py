from django.db import models

# Create your models here.

ALL_OPTIONS = (
	('both', 'Both'),
	('notary', 'Notary'),
	('bookkeeping', 'Bookkeeping'))

class Customer(models.Model):
	name = models.CharField(max_length=130)
	email = models.EmailField(blank=True)
	choices = models.CharField(max_length=100, choices=ALL_OPTIONS, null=True)
	phone = models.CharField(max_length=15)	
	detail = models.CharField(max_length=100, default="Add Details")
	def __str__(self):
		return self.name