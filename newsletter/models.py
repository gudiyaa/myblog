from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=100)
	author = models.ForeignKey(User)
	body = models.TextField()
	create_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title