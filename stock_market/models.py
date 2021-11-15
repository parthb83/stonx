from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Stock(models.Model):
	ticker = models.CharField(max_length=10)
	user = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.ticker