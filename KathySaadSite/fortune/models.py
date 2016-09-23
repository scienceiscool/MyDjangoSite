from django.db import models

# Create your models here.

class Fortune(models.Model):
	filename = models.CharField(max_length = 16)
	size = models.IntegerField()
	aphorism = models.CharField(max_length = 2147)
