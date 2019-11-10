from django.db import models
from django.contrib.auth.models import AbstractUser


class publisher(models.Model):
    note = models.CharField(max_length=500)
    uid = models.IntegerField()
     
    def __str__(self):
        return self.name
