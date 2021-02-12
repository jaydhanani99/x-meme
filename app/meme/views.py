from rest_framework import viewsets, mixins

from core.models import Meme
from meme import serializers

class MemeViewSet(viewsets.ModelViewSet):
    """Manage memes in database"""
    queryset = Meme.objects.all()
    serializer_class = serializers.MemeSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'PUT':
            serializer_class = serializers.MemeSerializerWithoutName

        return serializer_class

    def perform_create(self, serializer):
        """Create a new meme"""
        serializer.save()
