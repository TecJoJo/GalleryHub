from rest_framework import serializers
from galleryHub_api.models import Picture
class PictureSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)
    publish_date = serializers.DateField()

    def create(self,data):
        return Picture.objects.create(**data)
    
    def update(self,instance,data):
        instance.title = data.get("title",instance.title)
        instance.description = data.get("description",instance.description)
        instance.publish_date = data.get("publish_date",instance.publish_date)

        instance.save()
        return instance 
    
    