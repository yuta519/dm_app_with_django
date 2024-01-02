import django.db.models as models
from django_stubs_ext.db.models import TypedModelMeta

from app.models import BaseModel


class User(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=False, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta(TypedModelMeta):
        ordering = ["-created_at"]
        db_table = "users"
        app_label = "app"
