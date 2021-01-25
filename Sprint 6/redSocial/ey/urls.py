from django.urls import path

from . import views

urlpatterns = [
    path('', views.lobby, name='lobby'),
    path('userConfiguration/', views.configuration, name='configuration'),
    path('userInformation/', views.information, name='information'),

]