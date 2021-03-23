from django.db import models

# Create your models here.
class user(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    birth_date = models.DateField()
    address = models.CharField(max_length=100)
    image = models.ImageField()
    passeword = models.CharField(max_length=20)