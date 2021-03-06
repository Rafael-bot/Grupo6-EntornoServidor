from django.urls import path

from . import views

urlpatterns = [
    path('', views.profile_list, name='profile_list'),
    path('<slug:value>/',views.profile_detail, name='profile_detail'),
]