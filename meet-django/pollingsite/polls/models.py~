from django.db import models

class Poll(models.Model):
	question = models.CharField(max_length=200)

class Answer(models.Model):
	answerText = models.CharField(max_length=50)
	votes = models.IntegerField(default=0)
	poll = models.ForeignKey(Poll)
