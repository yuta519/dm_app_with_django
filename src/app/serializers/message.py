from rest_framework import serializers

from app.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("id", "user", "content", "created_at", "updated_at")
        read_only_fields = ("created_at", "updated_at")
