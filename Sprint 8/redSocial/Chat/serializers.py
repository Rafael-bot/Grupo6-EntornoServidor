from rest_framework import serializers
from .models import Chat


class ChatSerializer(serializers.Serializer):
    class Meta:
        model = Chat
        fields = ['id_chat', 'chat_text', 'date_text', 'user']

    id_chat = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    chat_text = serializers.CharField()
    date_text = serializers.DateTimeField()
    user = serializers.StringRelatedField(many=True)

    def create(self, validated_data):
        return Chat.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id_chat = validated_data.get('id_chat', instance.id_chat)
        instance.chat_text = validated_data.get('chat_text', instance.chat_text)
        instance.date_text = validated_data.get('date_text', instance.date_text)
        instance.username = validated_data.get('username', instance.user)
        instance.save()
        return instance
