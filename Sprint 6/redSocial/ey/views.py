from django.shortcuts import render

# Create your views here.

# Create your views here.
def lobby(request):
    context = {}
    return render(request, 'Ey/Index.html', context=context)

def configuration(request):
    context = {}
    return render(request, 'userConfiguration/configuration.html', context=context)
    
def information(request):
    context = {}
    return render(request, 'userInformation/Information.html', context=context)