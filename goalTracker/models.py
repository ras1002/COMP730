from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Goal(models.Model):
	title = models.CharField(max_length=255)
	amount = models.DecimalField(max_digits=6, decimal_places=2)
	current_saved = models.DecimalField(max_digits=6, decimal_places=2)
	description = models.CharField(max_length=255)
	owner = models.ForeignKey(User, related_name = "goal_owner")

	def __str__(self):
		return self.title + " - " + str(self.owner)
