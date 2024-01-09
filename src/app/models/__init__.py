from django.db import models


class BaseModel(models.Model):
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


from .message import *  # noqa: E402, F403
from .conversation import *  # noqa: E402, F403
