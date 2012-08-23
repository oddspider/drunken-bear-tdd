from django.db import models

class Poll(models.Model):
	questions = models.CharField(max_length=200)
