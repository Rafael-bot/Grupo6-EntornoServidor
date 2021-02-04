from django.shortcuts import render

# Create your views here.
def privateChat(request):
    context = {
        'Usuario1':'Jose',
        'Usuario2':'Lucrecia',
        'Mensaje1':'Hola Lucrecia',
        'Mensaje2': 'Hola Jose'
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
    context = {'Nombre':'Vladimir',
               'Contraseña':'******',
               'Email':'antortechin@gmail.com',
               'Fotografía':'Photo',
               'Teléfono':'666-666-666',
               'Biography':'Hello, I am a backend programer'}
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