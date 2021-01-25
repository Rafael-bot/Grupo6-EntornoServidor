from django.shortcuts import render

# Create your views here.
def postPhoto(request):
    context = {}
    return render(request, 'Cuentas/postPhoto/postPhoto.html', context=context)

def privateChat(request):
    context = {}
    return render(request, 'Cuentas/privateChat/privateChat.html', context=context)

def configuration(request):
    context = {}
    return render(request, 'Cuentas/userConfiguration/configuration.html', context=context)


def information(request):
    context = {}
    return render(request, 'Cuentas/userInformation/Information.html', context=context)


def login(request):
    context = {}
    return render(request, 'Cuentas/LoginRegister/Login.html', context=context)


def register(request):
    context = {}
    return render(request, 'Cuentas/LoginRegister/Register.html', context=context)