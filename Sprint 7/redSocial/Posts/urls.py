from django.urls import path

from . import views

urlpatterns = [
    path('postPhoto/', views.postPhoto, name="postPhoto"),
    path('personalPosts/', views.personalPosts, name='personalPosts'),
    path('publicPosts/', views.publicPosts, name='publicPosts'),
    path('comments/', views.comments, name='comments'),
]