from django import forms

from app.models import Conversation


class ConversationForm(forms.ModelForm):
    class Meta:
        model = Conversation
        fields = ["user1", "user2"]
