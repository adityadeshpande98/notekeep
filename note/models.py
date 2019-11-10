from django.db import models

class publisher(models.Model):
    note = models.CharField(max_length=200)
    