from django.db import models
from django_stubs_ext.db.models import TypedModelMeta


class BaseModel(models.Model):
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta(TypedModelMeta):
        ordering = ["-created_at"]
        db_table = "users"


class Message(BaseModel):
    content: models.TextField = models.TextField()
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)

    class Meta(TypedModelMeta):
        ordering = ["-created_at"]
        db_table = "messages"


class Conversation(BaseModel):
    user1 = models.ForeignKey(User, related_name="user1", on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name="user2", on_delete=models.CASCADE)
    # If we want to store a list of users, we can use JSONField
    # users = models.JSONField() # type: models.JSONField

    class Meta(TypedModelMeta):
        ordering = ["-created_at"]
        db_table = "conversations"
