from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views import generic
from rest_framework import viewsets

from app.models import Conversation
from app.serializers import ConversationSerializer


class ConversationListView(LoginRequiredMixin, generic.ListView):
    model = Conversation
    template_name = "conversations/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        conversations = Conversation.objects.all()
        for conversation in conversations:
            conversation.friend = (
                conversation.user2
                if conversation.user1 == self.request.user
                else conversation.user1
            )
        context["conversation_list"] = conversations
        return context


class ConversationDetailView(LoginRequiredMixin, generic.DetailView):
    model = Conversation
    template_name = "conversations/detail.html"


class ConversationApiViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(Q(user1=self.request.user) | Q(user2=self.request.user))
        user = self.request.query_params.get("user", None)
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset
