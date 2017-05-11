from django.db import models

# Create your models here.
class Task(models.Model):
	text = models.CharField(max_length=160)
	deadline = models.DateTimeField('deadline')
	percent = models.IntegerField(default = 0)
	
	def __str__(self):
		return self.text