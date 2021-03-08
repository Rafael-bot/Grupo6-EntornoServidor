from rest_framework import serializers
from .models import Chat


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"

    def create(self, validated_data):
        return Chat.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id_chat = validated_data.get('id_chat', instance.id_chat)
        instance.chat_text = validated_data.get('chat_text', instance.chat_text)
        instance.date_text = validated_data.get('date_text', instance.date_text)
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance
