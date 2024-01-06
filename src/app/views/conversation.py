from django.views import generic

from app.forms import ConversationForm
from app.models import Conversation


class ConversationListView(generic.ListView):
    model = Conversation
    template_name = "conversations/list.html"


class ConversationDetailView(generic.DetailView):
    model = Conversation
    template_name = "conversations/detail.html"


class ConversationCreateView(generic.CreateView):
    model = Conversation
    form_class = ConversationForm
    fields = ["user1", "user2"]
    template_name = "users/detail.html"
    success_url = "/"
