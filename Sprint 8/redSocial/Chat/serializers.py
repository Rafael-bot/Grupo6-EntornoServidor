from rest_framework import serializers
from .models import Chat

class ChatSerializer(serializers.Serializer):
    class Meta:
        model = Chat
        fields = ['id_chat', 'chat_text', 'date_text', 'username']

    id_chat = serializers.CharField(max_length=80)
    chat_text = serializers.CharField(max_length=2021)
    date_text = serializers.DateTimeField()
    #username = serializers.CharField(max_length=128)
    username = UserSerializer(read_only=True)

    def create(self, validated_data):
        return Chat.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id_chat = validated_data.get('id_chat', instance.id_chat)
        instance.chat_text = validated_data.get('chat_text', instance.chat_text)
        instance.date_text = validated_data.get('date_text', instance.date_text)
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance
