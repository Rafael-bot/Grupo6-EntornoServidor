from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('followers/', views.followers_list, name='followers_list'),
    path('token/', views.login, name='login_token'),
    #path('<slug:user_value>/followers/', views.followers_list_user, name='followers_list_users'),
    path('followers/<slug:value>/', views.followers_detail, name='followers_detail'),
    path('<slug:value>/', views.user_detail, name='user_detail'),
]
