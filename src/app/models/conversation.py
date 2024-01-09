from django.contrib.auth.models import User
from django.db.models import CASCADE, ForeignKey, Q
from django_stubs_ext.db.models import TypedModelMeta

from app.models import BaseModel


class Conversation(BaseModel):
    user1 = ForeignKey(User, related_name="user1", on_delete=CASCADE)
    user2 = ForeignKey(User, related_name="user2", on_delete=CASCADE)
    # If we want to store a list of users, we can use JSONField
    # users = JSONField() # type: JSONField

    class Meta(TypedModelMeta):
        ordering = ["-created_at"]
        db_table = "conversations"
        app_label = "app"

    def exists(users: list):
        return Conversation.objects.filter(
            Q(Q(user1=users[0]) & Q(user2=users[1]))
            | Q(Q(user1=users[1]) & Q(user2=users[0]))
        ).exists()
