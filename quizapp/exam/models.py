from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
	user = models.OneToOneField(User,unique=True,on_delete=models.CASCADE)
	question = models.CharField(max_length=400,unique=True)
	answer = models.CharField(max_length=300)

	def __str__(self):
		return str(self.question)

class Choices(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_a = models.CharField(max_length=200)
	choice_b = models.CharField(max_length=200)
	choice_c = models.CharField(max_length=200)

	def __str__(self):
		return str(self.question)

class Student(models.Model):
	user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	answer = models.CharField(max_length=250)

	def __str__(self):
		return str(self.question)