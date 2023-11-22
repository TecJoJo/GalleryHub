from rest_framework import serializers
from galleryHub_api.models import Picture
class PictureSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)
    publish_date = serializers.DateField()

    def create(self,data):
        return Picture.objects.create(**data)