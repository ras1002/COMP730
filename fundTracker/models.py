from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Fund(models.Model):
	balance = models.DecimalField(max_digits=6, decimal_places=2)
	owner = models.ForeignKey(User)

	def __str__(self):
		return "{}: {}".format(self.owner, self.balance)

class Transaction(models.Model):
	amount = models.DecimalField(max_digits=6, decimal_places=2)
	date = models.DateTimeField(auto_now=True)
	category = models.CharField(max_length=64)
	owner = models.ForeignKey(User)

	def __str__(self):
		return "{}: {}".format(self.owner, self.amount)
