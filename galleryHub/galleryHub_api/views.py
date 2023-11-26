from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from galleryHub_api.models import Picture
from galleryHub_api.serializer import PictureSerializer

# Create your views here.

@api_view(['GET'])
def pictureList(request):
    pictures = Picture.objects.all()
    serializer = PictureSerializer(pictures, many = True )
    return Response(serializer.data)


@api_view(['POST'])
def picture_upload(request):
    serializer = PictureSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def picture_detail(request, pk):
    picture = Picture.objects.get(pk=pk)
    if request.method == "GET":
        serializer = PictureSerializer(picture)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = PictureSerializer(picture,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    if request.method == "DELETE":
        picture.delete()

        
        return Response({"deleted":True})    
