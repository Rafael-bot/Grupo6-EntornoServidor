from django.urls import path

from . import views

urlpatterns = [
    path('', views.history_list, name='history_list'),
    path('<slug:value>/',views.history_detail, name='history_detail'),
]