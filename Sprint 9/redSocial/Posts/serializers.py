from rest_framework import serializers
from .models import Posts


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'


    def create(self, validated_data):

        return Posts.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id_posts = validated_data.get('id_posts', instance.id_posts)
        instance.number_posts = validated_data.get('number_posts', instance.number_posts)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.description = validated_data.get('description', instance.description)
        instance.post_date = validated_data.get('post_date', instance.post_date)
        instance.public_or_private = validated_data.get('public_or_private', instance.public_or_private)
        instance.username = validated_data.get('username', instance.username)
        instance.id_coments = validated_data.get('id_coments', instance.id_coments)
        instance.save()
        return instance