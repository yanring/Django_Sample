# coding=utf-8
from django.db import models


# Create your models here.
class User(models.Model):
    uid = models.AutoField(max_length=50,primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username

