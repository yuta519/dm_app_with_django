from django.db import models
from django_stubs_ext.db.models import TypedModelMeta

from app.models import BaseModel


class Conversation(BaseModel):
    user1 = models.ForeignKey(
        "app.User", related_name="user1", on_delete=models.CASCADE
    )
    user2 = models.ForeignKey(
        "app.User", related_name="user2", on_delete=models.CASCADE
    )
    # If we want to store a list of users, we can use JSONField
    # users = models.JSONField() # type: models.JSONField

    class Meta(TypedModelMeta):
        ordering = ["-created_at"]
        db_table = "conversations"
        app_label = "app"
