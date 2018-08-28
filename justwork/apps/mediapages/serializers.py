from rest_framework import serializers
from .models import (Page, Block)
from rest_framework.reverse import reverse


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = (
            'title', 'order_number', 'counter',
            'text',
            'audio', 'bitrate',
            'video', 'video_sub',
        )


class PageSerializer(serializers.ModelSerializer):
    block = BlockSerializer(many=True, required=False)
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return reverse('mediapages-list') + str(obj.id) + '/'

    class Meta:
        model = Page
        fields = ('id', 'order_number', 'title', 'block', 'url')
