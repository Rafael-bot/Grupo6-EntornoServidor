from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [

    path('userConfiguration/', views.configuration, name='configuration'),
    path('userInformation/', views.information, name='information'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('privateChat/', views.privateChat, name='privateChat'),

    path('<str:user>/', views.detail_user,name='detalleUser')
]