from django.db import models

class Shorts(models.Model):
	incomingurl= models.CharField(max_length=5000)
	outgoingurl1= models.CharField(max_length=5000)
	updated = models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=True,auto_now_add=False)


	def __str__(self):
		return self.incomingurl
