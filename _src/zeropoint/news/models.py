from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    abstract = models.TextField(null=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
