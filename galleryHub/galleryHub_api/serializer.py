from rest_framework import serializers

class PictureSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)
    publish_date = serializers.DateField()