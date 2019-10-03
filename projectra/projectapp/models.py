from django.db import models

# Create your models here.

class studentformsave(models.Model):
    applicant_name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=30)
    dateofbirth = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    departsubject = models.CharField(max_length=30)