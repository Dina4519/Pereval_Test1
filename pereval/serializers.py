from pereval.models import *
from rest_framework import serializers


class PerevalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        fields = [
            'url',
            'id',
            'beauty_title',
            'title',
            'other_titles',
            'connect',
            'add_time',
            'user',
            'coords',
            'level',
            'images',

        ]

