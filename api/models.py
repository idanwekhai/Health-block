from django.db import models

# Create your models here.
class Patient(models.Model):
	address = models.CharField(max_length=44)
	bloodPressure = models.FloatField()
	temperature = models.FloatField()
	weight = models.FloatField()
	height = models.FloatField()

	def __str__(self):
		return self.address