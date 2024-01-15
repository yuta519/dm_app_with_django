from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from app.models import Conversation


class MyAdminSite(admin.AdminSite):
    site_title = "My Custom Admin Title"
    site_header = "My Custom Admin Header"
    index_title = "My Custom Admin Index Title"


class ConversationModelAdmin(admin.ModelAdmin):
    list_display = ("id",)


admin_site = MyAdminSite(name="myadmin")

admin_site.register(Conversation, ConversationModelAdmin)
admin_site.register(User, UserAdmin)
