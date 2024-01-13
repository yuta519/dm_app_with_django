from django.contrib.admin import AdminSite

from app.models import Conversation, Message, User


class MyAdminSite(AdminSite):
    site_title = "My Custom Admin Title"
    site_header = "My Custom Admin Header"
    index_title = "My Custom Admin Index Title"


admin_site = MyAdminSite(name="myadmin")

admin_site.register(Conversation)
admin_site.register(Message)
admin_site.register(User)
