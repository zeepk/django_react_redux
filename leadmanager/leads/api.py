from leads.models import (Lead, User, Entry)
from rest_framework import viewsets, permissions
from .serializers import (LeadSerializer, UserSerializer, EntrySerializer)


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EntrySerializer
