from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from galleryHub_api.models import Picture
from galleryHub_api.serializer import PictureSerializer
# Create your views here.

@api_view(['GET'])
def pictureList(request):
    pictures = Picture.objects.all()
    mappedPictureList = PictureSerializer(pictures, many = True )
    return Response(mappedPictureList.data)


@api_view(['POST'])
def picture_upload(request):
    mappedPictureUpload = PictureSerializer(data = request.data)
    if mappedPictureUpload.is_valid():
        mappedPictureUpload.save()
        return Response({"upload succeeded",mappedPictureUpload})
    else:
        return Response(mappedPictureUpload.errors)
