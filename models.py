from django.db import models

# Create your models here.
class DEPT(models.Model):
    DEPTNO=models.IntegerField(max_length=10)
    DEPTNAME=models.CharField(max_length=10)
    DEPTLOC=models.CharField(max_length=10)
    
