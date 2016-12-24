# coding=utf-8
from django.db import models
from login.models import User


# Create your models here.
class Device(models.Model):
    deviceId = models.AutoField(max_length=20, primary_key=True)
    uid = models.ForeignKey(User, related_name='+')
    state = models.CharField(max_length=50)
    deviceName = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

    # python2使用__unicode__, python3使用__str__
    def __unicode__(self):
        return self.title

class Repair(models.Model):
    repairId = models.AutoField(max_length=20, primary_key=True)
    deviceId = models.ForeignKey(Device, related_name='+')
    uid = models.ForeignKey(User, related_name='+')
    date = models.DateTimeField(auto_now_add = True)
    note = models.CharField(max_length=50)
    finished = models.CharField(max_length=50)

    # python2使用__unicode__, python3使用__str__
    def __unicode__(self):
        return self.title


class lend(models.Model):
    lendId = models.AutoField(max_length=20, primary_key=True)
    deviceId = models.ForeignKey(Device, related_name='+')
    uid = models.ForeignKey(User, related_name='+')
    date = models.DateTimeField(auto_now_add = True)
    note = models.CharField(max_length=50)
    finished = models.CharField(max_length=50)
    # python2使用__unicode__, python3使用__str__
    def __unicode__(self):
        return self.title


class discard(models.Model):
    discardId = models.AutoField(max_length=20, primary_key=True)
    deviceId = models.ForeignKey(Device, related_name='+')
    uid = models.ForeignKey(User, related_name='+')
    date = models.DateTimeField(auto_now_add = True)
    note = models.CharField(max_length=50)
    finished = models.CharField(max_length=50)

    # python2使用__unicode__, python3使用__str__
    def __unicode__(self):
        return self.title