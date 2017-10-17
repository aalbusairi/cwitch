from django.db import models
from django.contrib.auth.models import User

class Games(models.Model):
	name = models.CharField(max_length=20)
	description = models.TextField(null = True, blank=True)

	def __str__(self):
		return self.name
