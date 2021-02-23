from rest_framework import serializers
from .models import Histories


class HistorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Histories
        fields = '__all__'

    def create(self, validated_data):

        return Histories.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id_history = validated_data.get('id_history', instance.id_history)
        instance.history = validated_data.get('history', instance.history)
        instance.date_of_history = validated_data.get('date_of_history', instance.date_of_history)
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance
