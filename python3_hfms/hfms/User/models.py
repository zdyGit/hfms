from django.db import models

# Create your models here.
class Sys_User(models.Model):
	userID = models.CharField(max_length=20)
	userName = models.CharField(max_length=30)
	pwd = models.CharField(max_length=60)
	createDate = models.DateTimeField()
		