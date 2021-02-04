from django.shortcuts import render


# Create your views here.
def postPhoto(request):
    context = {'Imagen': 'Imagen posteada'}
    return render(request, 'Posts/postPhoto/postPhoto.html', context=context)


def personalPosts(request):
    context = {
        'foto': 'Fotografica post personal',
        'username': 'Manuel',
        'descripción': 'En el campo',
    }
    return render(request, 'Posts/personalPosts/personalPosts.html', context=context)


def publicPosts(request):
    context = {
        'foto': 'Fotografica post público',
        'username': 'Manuel',
        'descripción': 'En la playa',
    }
    return render(request, 'Posts/publicPosts/publicPosts.html', context=context)


def comments(request):
    context = {
        'username': 'Manuel',
        'comentario': 'Bonita fotografía'
    }
    return render(request, 'Posts/comments/comments.html', context=context)
