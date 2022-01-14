from rest_framework import serializers
from .models import Songs

class SongSerializers(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ['id', 'title', 'artist', 'album', 'genre', 'release_date']