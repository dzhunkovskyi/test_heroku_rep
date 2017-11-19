from django.db import models
import os
import json
from datetime import datetime

# Create your models here.
class Post(models.Model):

	post_title = models.CharField(max_length=200)
	post_content = models.TextField(default='')
	post_likes = models.IntegerField(default=0)
	post_users_liked = models.CharField(default='[]', max_length=200)
	post_image = models.ImageField(upload_to='static')
	post_date = models.DateTimeField(default=datetime.now)

	def add_user(self, user_name):
		list_of_user = json.loads(self.post_users_liked)
		list_of_user.append(user_name)
		print('LIST OF USER = ', list_of_user)
		self.post_users_liked = json.dumps(list_of_user)

	def delete_user(self, user_name):
		list_of_user = json.loads(self.post_users_liked)
		list_of_user.remove(user_name)
		print('LIST OF USER = ', list_of_user)
		self.post_users_liked = json.dumps(list_of_user)

	def return_list_of_user(self):
		list_of_user = json.loads(self.post_users_liked)
		return list_of_user