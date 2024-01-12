from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from rest_framework import viewsets

from app.models import Conversation
from app.serializers import ConversationSerializer


class ConversationListView(LoginRequiredMixin, generic.ListView):
    model = Conversation
    template_name = "conversations/list.html"


class ConversationDetailView(generic.DetailView):
    model = Conversation
    template_name = "conversations/detail.html"


class ConversationApiViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def get_queryset(self):
        queryset = Conversation.objects.all()
        user = self.request.query_params.get("user", None)
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset
