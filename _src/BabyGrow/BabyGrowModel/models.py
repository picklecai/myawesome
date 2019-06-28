from django.db import models

# Create your models here.


class BabyInfo(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=2, default='男')
    birthtime = models.CharField(max_length=15)
    momemail = models.CharField(max_length=40)
    settingtime = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class NoteRecord(models.Model):
    time = models.CharField(max_length=20)
    age = models.CharField(max_length=5)
    record = models.CharField(max_length=150)

    def __str__(self):
        return self.record
