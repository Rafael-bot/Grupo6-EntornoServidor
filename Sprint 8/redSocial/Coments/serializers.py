from rest_framework import serializers
from .models import Coments


class ComentSerializer(serializers.Serializer):
    class Meta:
        model = Coments
        fields = ['id_coments', 'last_name', 'email', 'username']

    id_coments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    coment_text = serializers.CharField()
    date_of_coment = serializers.DateTimeField()
    number_likes = serializers.IntegerField()
    username = serializers.StringRelatedField(many=True)

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
