from rest_framework import serializers

from app.models import Conversation


class ConversationSerializer(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ("id", "messages", "user1", "user2", "created_at", "updated_at")
        read_only_fields = ("created_at", "updated_at")

    def get_messages(self, obj: Conversation):
        from app.serializers import MessageSerializer

        return MessageSerializer(obj.messages, many=True).data

    def validate(self, data):
        user1 = data.get("user1")
        user2 = data.get("user2")
        if Conversation.exists(users=[user1, user2]):
            raise serializers.ValidationError(
                {"error": "A conversation between these users already exists."}
            )
        return data
