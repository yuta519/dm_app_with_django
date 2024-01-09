from django.contrib.auth.models import User
from django.db import models
from app.models import BaseModel


class Message(BaseModel):
    content: models.TextField = models.TextField()
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    conversation = models.ForeignKey(
        "app.Conversation", related_name="messages", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["-created_at"]
        db_table = "messages"
        app_label = "app"
