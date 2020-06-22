from django.urls import path
from . import views

app_name = 'solution'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.Indexview.as_view(), name='index'),
    path('solution-detail/<int:id>', views.solution_detail, name='solution_detail')
]
