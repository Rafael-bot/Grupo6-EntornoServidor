from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Coments
from .serializers import ComentSerializer


# Create your views here.

@csrf_exempt
def coment_list(request):
    if request.method == 'GET':
        coment = Coments.objects.all()
        serializer = ComentSerializer(coment, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ComentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=204)


@csrf_exempt
def coment_detail(request, value):
    try:
        coment = Coments.objects.get(id_coments=value)
    except Coments.DoesNotExist:
        return HttpResponse(status=404)

    #Request para consultar
    if request.method == 'GET':
        serializer = ComentSerializer(coment)
        return JsonResponse(serializer.data, safe=False, status=200)
    #Request para modificar
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ComentSerializer(coment,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=204)
    #Request para eliminar
    elif request.method=='DELETE':
        try:
            coment.delete()
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=409)