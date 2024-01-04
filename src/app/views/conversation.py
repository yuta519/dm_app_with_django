from django.views import generic

from app.models import Conversation


class ConversationListView(generic.ListView):
    model = Conversation
    template_name = "conversations/list.html"


class ConversationDetailView(generic.DetailView):
    model = Conversation
    template_name = "conversations/detail.html"


class ConversationCreateView(generic.CreateView):
    model = Conversation
    fields = ["name", "description"]
