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
        return Response(mappedPictureUpload.data)
    else:
        return Response(mappedPictureUpload.errors)

@api_view(['GET','PUT','DELETE'])
def picture_detail(request, pk):
    picture = Picture.objects.get(pk=pk)
    if request.method == "GET":
        mappedPicture = PictureSerializer(picture)
        return Response(mappedPicture.data)
    if request.method == "PUT":
        modifyPicture = PictureSerializer(picture,request.data)
        if modifyPicture.is_valid():
            modifyPicture.save()
            return Response(modifyPicture.data)
        else:
            return Response(modifyPicture.errors)
    if request.method == "DELETE":
        deletePicture = PictureSerializer(picture)
        if modifyPicture.is_valid():
            deletePicture.save()
            return Response(deletePicture.data)    
