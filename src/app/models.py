from django.db import models
from django_stubs_ext.db.models import TypedModelMeta


class User(models.Model):
    first_name: str
    last_name: str
    email: str
    password: str
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    class Meta(TypedModelMeta):
        ordering = ["-created_at"]
        db_table = "users"


class Message(models.Model):
    content: models.TextField = models.TextField()
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(TypedModelMeta):
        ordering = ["-created_at"]
        db_table = "messages"


class Conversation(models.Model):
    user1 = models.ForeignKey(User, related_name="user1", on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name="user2", on_delete=models.CASCADE)
    # If we want to store a list of users, we can use JSONField
    # users = models.JSONField() # type: models.JSONField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(TypedModelMeta):
        ordering = ["-created_at"]
        db_table = "conversations"
