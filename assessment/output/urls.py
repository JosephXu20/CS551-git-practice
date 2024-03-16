from django.urls import path
from . import views

urlpatterns = [
path('', views.data_list, name='data_list'),
path('metadata/<str:tableName>/', views.data_detail, name= 'data_detail'),
]