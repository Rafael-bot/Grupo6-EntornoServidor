from rest_framework import serializers
from .models import User, Followers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

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
        fields = ('id_followers', 'my_follows', 'my_followers','username','username_id')

    id_followers = serializers.CharField(max_length=80)
    my_follows = serializers.IntegerField()
    my_followers = serializers.IntegerField()
    username_id = serializers.CharField(max_length=128)


    def create(self, validated_data):
        return Followers.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id_followers = validated_data.get('id_followers', instance.id_followers)
        instance.my_follows = validated_data.get('my_follows', instance.my_follows)
        instance.my_followers = validated_data.get('my_followers', instance.my_followers)
        instance.username = validated_data.get('username', instance.username)
        instance.username_id = validated_data.get('username_id', instance.username_id)
        instance.save()
        return instance