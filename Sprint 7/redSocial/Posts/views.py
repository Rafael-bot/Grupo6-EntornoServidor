from django.http import Http404
from django.shortcuts import render
from .models import Foto,Coments

# Create your views here.
def postPhoto(request):
    context = {'Imagen': 'Imagen posteada'}
    return render(request, 'Posts/postPhoto/postPhoto.html', context=context)


def personalPosts(request):
    post = Foto.objects.filter(cat='private')
    context = {
        'personal':post
    }
    return render(request, 'Posts/personalPosts/personalPosts.html', context=context)


def publicPosts(request):
    post = Foto.objects.filter(cat='public')
    context = {
        'public': post
    }
    return render(request, 'Posts/publicPosts/publicPosts.html', context=context)


def comments(request):
    comment = Coments.objects.order_by('date')
    context = {
        'comments': comment
    }
    return render(request, 'Posts/comments/comments.html', context=context)

def detail_postPersonal(request,user,id1):
    try:
        post = Foto.objects.get(pk=id1)
        postUser = Foto.objects.select_related('username').get(username_id=user)
    except Foto.DoesNotExist:
        raise Http404("No existe en la base de datos")
    return render(request, 'Posts/personalPosts/personalPost.html', {'foto': post})

def detail_postPublic(request,id2):
    try:
        post = Foto.objects.get(pk=id2)
        comments = Coments.objects.filter(comment_code_id=id2)
    except Foto.DoesNotExist:
        raise Http404("No existe en la base de datos")
    return render(request, 'Posts/publicPosts/publicPost.html', {'foto': post, 'comment': comments})