from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import User, Followers
from .serializers import UserSerializer, FollowSerializer


# Create your views here.
@csrf_exempt
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
