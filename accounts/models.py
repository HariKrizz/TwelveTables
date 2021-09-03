from django.db import models
from django.db.models.deletion import CASCADE


class Account(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    uname = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=50,unique=True)
    passwd= models.CharField(max_length=50)

    def __str__(self):
        return self.uname

class Acc_Data(models.Model):
    username = models.CharField(max_length=30)
    key = models.CharField(max_length=30)
    value = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        unique_together = ('username','key')



