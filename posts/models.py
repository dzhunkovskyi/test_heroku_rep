from django.db import models

# Create your models here.
class Post(models.Model):

	post_title = models.CharField(max_length=200)
	post_content = models.TextField(default='')
	post_likes = models.IntegerField(default=0)
	post_image = models.ImageField(upload_to='static')