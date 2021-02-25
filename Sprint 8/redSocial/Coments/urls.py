from django.urls import path

from . import views

urlpatterns = [
    path('', views.coment_list, name='coments_list'),
    path('<slug:value>/', views.coment_detail, name='coments_detail'),
]
