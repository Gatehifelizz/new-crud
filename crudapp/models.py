from django.db import models


# Create your models here.
class Employee\
            (models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    work_id = models.CharField(max_length=30)
    contact = models.CharField(max_length=20)
    department = models.CharField(max_length=35)
    shift= models.CharField(max_length=20)
    class Meta:
        db_table = 'workers'
