from django.http import Http404
from django.shortcuts import render
from .models import Cuentas,Chat

# Create your views here.
def privateChat(request):
    chat = Chat.objects.order_by('date')
    context = {
        'chats':chat
    }
    return render(request, 'Cuentas/privateChat/privateChat.html', context=context)

def configuration(request):
    context = {'Nombre':'Vladimir',
               'Contraseña':'******',
               'Email':'antortechin@gmail.com',
               'Fotografía':'Photo',
               'Teléfono':'666-666-666',
               'Biography':'Hello, I am a backend programer'}
    return render(request, 'Cuentas/userConfiguration/configuration.html', context=context)


def information(request):
    cuent = Cuentas.objects.order_by('username')
    context = {'cuentas':cuent}
    return render(request, 'Cuentas/userInformation/Information.html', context=context)


def login(request):
    context = {
        'username   ':'Jose',
        'contrasenna': '123'
    }
    return render(request, 'Cuentas/LoginRegister/Login.html', context=context)


def register(request):
    context = {
        'username':'Jose',
        'contrasenna': '123',
        'contrasenna_confirm': '123'
    }
    return render(request, 'Cuentas/LoginRegister/Register.html', context=context)

def detail_user(request,user):
    try:
        cuent = Cuentas.objects.get(pk=user)
    except Cuentas.DoesNotExist:
        raise Http404("El usuario no existe en la base de datos")
    return render(request, 'Cuentas/userInformation/InfoUser.html', {'cuenta': cuent})