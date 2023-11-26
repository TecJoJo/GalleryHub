# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from galleryHub_api.models import Picture
# from galleryHub_api.serializer import PictureSerializer
# from rest_framework import status

# # Create your views here.

# @api_view(['GET'])
# def pictureList(request):
#     pictures = Picture.objects.all()
#     serializer = PictureSerializer(pictures, many = True )
#     return Response(serializer.data)


# @api_view(['POST'])
# def picture_upload(request):
#     serializer = PictureSerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def picture_detail(request, pk):
#     try:
#         picture = Picture.objects.get(pk=pk)
#     except:
#         return Response({"Error":"picture not found"},status=status.HTTP_404_NOT_FOUND)
#     if request.method == "GET":
#         serializer = PictureSerializer(picture)
#         return Response(serializer.data)
#     if request.method == "PUT":
#         serializer = PictureSerializer(picture,request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == "DELETE":
#         picture.delete()

        
#         return Response(status=status.HTTP_204_NO_CONTENT)    

#---------------------------------------->>>>>>>>>>>>>>
# refactor to classbased view 


from rest_framework.views import APIView
from galleryHub_api.models import Picture
from galleryHub_api.serializer import PictureSerializer
from rest_framework.response import Response
from rest_framework import status

class PictureList(APIView):
    def get(self,request):
        pictures = Picture.objects.all()
        serializer = PictureSerializer(pictures, many = True )
        return Response(serializer.data)

class PictureUpload(APIView):
    def post(self,request):
        serializer = PictureSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class PictureDetail(APIView):
    def get_picture_by_pk(self,pk):
        try:
            picture = Picture.objects.get(pk=pk)
            return picture
            
        except:
            return Response({"Error":"picture not found"},status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        try:
            picture = Picture.objects.get(pk=pk)
            serializer = PictureSerializer(picture)
            return Response(serializer.data)
        except:
            return Response({
                'error': 'Picture does not exist'
            }, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        
        picture = self.get_picture_by_pk(pk)
        serializer = PictureSerializer(picture,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        picture = self.get_picture_by_pk(pk)
        picture.delete()
        return Response({"deleted":True},status=status.HTTP_204_NO_CONTENT)    

        