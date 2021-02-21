from rest_framework import serializers
from .models import Coments
from Cuentas.serializers import UserSerializer


class ComentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coments
        fields = "__all__"

    def create(self, validated_data):
        return Coments.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id_coments = validated_data.get('id_coments', instance.id_coments)
        instance.coment_text = validated_data.get('coment_text', instance.coment_text)
        instance.date_of_coment = validated_data.get('date_of_coment', instance.date_of_coment)
        instance.number_likes = validated_data.get('number_likes', instance.number_likes)
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance
