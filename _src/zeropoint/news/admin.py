from django.contrib import admin
from .models import *

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date')
    list_per_page = 10


class CateAdmin(admin.ModelAdmin):
    list_display = ('name', 'article_count')

    def article_count(self, obj):
        return Post.objects.filter(category=obj).count()


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CateAdmin)
