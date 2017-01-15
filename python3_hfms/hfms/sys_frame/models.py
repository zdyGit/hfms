from django.db import models

# Create your models here.
class Syspage(models.Model):
    pagetitle = models.CharField(max_length=30)
    pageurl = models.CharField(max_length=30)
    pagesort = models.IntegerField()
    pagecreatedate = models.DateTimeField()
    pagefatherid = models.IntegerField() 
    pagedeleteflag = models.IntegerField()
