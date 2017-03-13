from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
	title = models.CharField(max_length=100)
	author = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
	body = models.TextField()
	create_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title