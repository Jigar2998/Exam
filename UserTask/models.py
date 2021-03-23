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

    def __str__(self):
        return self.fname

class task_assign(models.Model):
    task_name = models.CharField(max_length=25)
    task_detail = models.CharField(max_length=25)
    assign_user = models.ForeignKey('user', on_delete=models.CASCADE)
    stat = (('Working','Working'),('Working Done','Working Done'))
    status = models.CharField(max_length=25, choices=stat, default='Working')
    assign_work_date = models.DateField(auto_now=True)
    due_date = models.DateField()

class contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    message = models.CharField(max_length=100)