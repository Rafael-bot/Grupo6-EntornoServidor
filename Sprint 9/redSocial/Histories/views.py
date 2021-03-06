from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

from .models import Histories
from .serializers import HistorieSerializer


# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def history_list(request):
    if request.method == 'GET':
        history = Histories.objects.all()
        serializer = HistorieSerializer(history, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HistorieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=204)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def history_detail(request, value):
    try:
        history= Histories.objects.get(id_history=value)
    except Histories.DoesNotExist:
        return HttpResponse(status=404)

    # Request para consultar
    if request.method == 'GET':
        serializer = HistorieSerializer(history)
        return JsonResponse(serializer.data, safe=False, status=200)
    # Request para modificar
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = HistorieSerializer(history, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=204)
    # Request para eliminar
    elif request.method == 'DELETE':
        try:
            history.delete()
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=409)