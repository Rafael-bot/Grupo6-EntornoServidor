from django.urls import path

from . import views

urlpatterns = [
    path('postPhoto/', views.postPhoto, name="postPhoto"),
    path('personalPosts/', views.personalPosts, name='personalPosts'),
    path('publicPosts/', views.publicPosts, name='publicPosts'),
    path('comments/', views.comments, name='comments'),

    path('<str:user>/<int:id1>/', views.detail_postPersonal, name='detallepersonalPost'),
    path('<int:id2>/', views.detail_postPublic, name='detallepostPublic')
]
