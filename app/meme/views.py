from rest_framework import viewsets, mixins, pagination
from rest_framework.response import Response

from core.models import Meme
from meme import serializers

class MemePagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    def get_paginated_response(self, data):
        return Response({
            # 'next_page': self.get_next_link(),
            # 'previous_page': self.get_previous_link(),
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current': self.page.number,
            'data': data
        })

class MemeViewSet(viewsets.ModelViewSet):
    """Manage memes in database"""
    queryset = Meme.objects.all()
    serializer_class = serializers.MemeSerializer
    pagination_class = MemePagination

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'PUT':
            serializer_class = serializers.MemeSerializerWithoutName

        return serializer_class

    def perform_create(self, serializer):
        """Create a new meme"""
        serializer.save()
