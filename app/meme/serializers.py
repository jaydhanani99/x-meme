from rest_framework import serializers

from core.models import Meme


class MemeSerializer(serializers.ModelSerializer):
    """Serializer for Meme Objects"""

    class Meta:
        model = Meme
        fields = ('id', 'name', 'url', 'caption')
        read_only_fields = ('id',)
    
class MemeSerializerWithoutName(serializers.ModelSerializer):
    """Serializer for Meme Objects without name field"""

    class Meta:
        model = Meme
        fields = ('id', 'name', 'url', 'caption')
        read_only_fields = ('id','name')

        

