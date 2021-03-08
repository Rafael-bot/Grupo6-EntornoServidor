from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes, api_view
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

from .models import Profile
from .serializers import PostsSerializer


# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def profile_list(request):
    if request.method == 'GET':
        profile = Profile.objects.all()
        serializer = PostsSerializer(profile, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=204)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def profile_detail(request, value):
    try:
        profile= Profile.objects.get(id_profile=value)
    except Profile.DoesNotExist:
        return HttpResponse(status=404)

    # Request para consultar
    if request.method == 'GET':
        serializer = PostsSerializer(profile)
        return JsonResponse(serializer.data, safe=False, status=200)
    # Request para modificar
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PostsSerializer(profile, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=204)
    # Request para eliminar
    elif request.method == 'DELETE':
        try:
            profile.delete()
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=409)