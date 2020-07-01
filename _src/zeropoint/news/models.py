from django.db import models
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Category(models.Model):
    """docstring for ClassName"""
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'
        ordering = ['id']


class Post(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    image = models.ImageField(upload_to='', null=True)
    abstract = models.TextField(null=True, max_length=200)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
