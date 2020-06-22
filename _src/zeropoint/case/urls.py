from django.urls import path
from . import views

app_name = 'case'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.Indexview.as_view(), name='index'),
    path('case-detail/<int:id>', views.case_detail, name='case_detail')
]
