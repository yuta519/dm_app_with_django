from django_stubs_ext.db.models import TypedModelMeta

from app.models import BaseModel


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
        app_label = "app"
