from ..models import Message
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('email', 'message', 'time_create', 'time_update')
