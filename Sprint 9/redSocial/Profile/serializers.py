from rest_framework import serializers
from .models import Profile


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


    def create(self, validated_data):

        return Profile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id_profile = validated_data.get('id_profile', instance.id_profile)
        instance.biography = validated_data.get('biography', instance.biography)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.username = validated_data.get('username', instance.username)
        instance.id_posts = validated_data.get('id_posts', instance.id_posts)
        instance.id_followers = validated_data.get('id_followers', instance.id_followers)
        instance.save()
        return instance