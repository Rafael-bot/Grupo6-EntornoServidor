from django.shortcuts import render

# Create your views here.
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