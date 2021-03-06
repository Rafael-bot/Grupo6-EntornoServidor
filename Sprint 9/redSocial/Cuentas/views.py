from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

from .models import User, Followers
from .serializers import UserSerializer, FollowSerializer
#Auth
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.response import Response



# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_list(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=204)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_detail(request, value):
    try:
        user = User.objects.get(username=value)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    # Request para consultar
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, safe=False, status=200)
    # Request para modificar
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=204)
    # Request para eliminar
    elif request.method == 'DELETE':
        try:
            user.delete()
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=409)


@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def followers_list(request):
    if request.method == 'GET':
        r = str(request)
        if r.find('?user=')>=1:
            user = request.GET.get('user')
            follow = Followers.objects.filter(username=user).order_by('username')
        else:
            follow = Followers.objects.all()

        serializer = FollowSerializer(follow, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FollowSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=204)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def followers_detail(request, value):
    try:
        follow = Followers.objects.get(id_followers=value)
    except Followers.DoesNotExist:
        return HttpResponse(status=404)

    # Request para consultar
    if request.method == 'GET':
        serializer = FollowSerializer(follow)
        return JsonResponse(serializer.data, safe=False, status=200)
    # Request para modificar
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FollowSerializer(follow, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=204)
    # Request para eliminar
    elif request.method == 'DELETE':
        try:
            follow.delete()
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=409)

@api_view(['POST','GET'])
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
        user = AuthUser.objects.get(username=username)
    except AuthUser.DoesNotExist:
        return HttpResponse(status=404)

    pwd_valid = check_password(password, user.password)

    if not pwd_valid:
        return HttpResponse(status=409)

    token, create = Token.objects.get_or_create(user=user)
    #print(token.key)
    return Response(token.key)

