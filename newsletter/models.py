from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.
# class SignUp(models.Model):
# 	email=models.EmailField(max_length=200)
# 	full_name=models.CharField(max_length=100,blank=True,null=True)
# 	timestamp=models.DateTimeField(auto_now=True)	

# 	def __str__(self):
# 		return self.email

class Post(models.Model):
	title = models.CharField(max_length=100)
	author = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
	body = models.TextField()
	create_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title