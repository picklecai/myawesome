from django.db import models

# Create your models here.


class babyinfo(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=2, default='男')
    birthtime = models.DateField(default='2015-01-01')
