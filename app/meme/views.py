from rest_framework import viewsets, mixins

from core.models import Meme
from meme import serializers

class MemeViewSet(viewsets.ModelViewSet):
    """Manage memes in database"""
    queryset = Meme.objects.all()
    serializer_class = serializers.MemeSerializer

    def perform_create(self, serializer):
        """Create a new meme"""
        serializer.save()
