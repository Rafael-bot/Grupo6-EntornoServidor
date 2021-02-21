from rest_framework import serializers
from .models import User, Followers

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    username = serializers.CharField(max_length=128)
    password = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class FollowSerializer(serializers.Serializer):
    class Meta:
        model = Followers
        fields = ['id_followers', 'my_follows', 'my_followers', 'username']

    id_followers = serializers.CharField()
    my_follows = serializers.CharField()
    my_followers = serializers.EmailField()
    username = UserSerializer

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id_followers = validated_data.get('id_followers', instance.id_followers)
        instance.my_follows = validated_data.get('my_follows', instance.my_follows)
        instance.my_followers = validated_data.get('my_followers', instance.my_followers)
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance