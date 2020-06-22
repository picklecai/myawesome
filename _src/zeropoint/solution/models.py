from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class SoluArcs(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='', null=True)
    abstract = models.TextField(null=True, max_length=200)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title
