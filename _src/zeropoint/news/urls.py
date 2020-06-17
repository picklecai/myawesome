from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.Indexview.as_view(), name='index'),
    path('article-detail/<int:id>', views.article_detail, name='article_detail')
    # path('article-detail/<int:pk>', views.PostDetailView.as_view(), name='article_detail')
]
