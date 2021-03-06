from django.urls import path

from . import views

urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    path('<slug:value>/',views.posts_detail, name='posts_detail'),
]
