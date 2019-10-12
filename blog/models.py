from django.db import models

# Create your models here.
#allows us to store data in a very specific way

class BlogPost(models.Model):
	#need to declare what this file is
	title = models.TextField()
	#blog를 settings.py의 Installed App 에 'blog'를 추가
	#cmd에서 python manage.py makemigrations과 python manage.py migrate 추가
	content = models.TextField(null = True, blank = True)