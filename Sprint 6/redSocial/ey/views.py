from django.shortcuts import render

# Create your views here.

# Create your views here.
def lobby(request):
    context = {}
    return render(request, 'Ey/Index.html', context=context)

