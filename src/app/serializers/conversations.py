from rest_framework import serializers

from app.models import Conversation


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ("user1", "user2", "created_at", "updated_at")
        read_only_fields = ("created_at", "updated_at")
