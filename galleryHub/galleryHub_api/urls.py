
from django.contrib import admin
from django.urls import path
#from galleryHub_api.views import pictureList, picture_upload, picture_detail
from galleryHub_api.views import PictureList, PictureUpload, PictureDetail

urlpatterns = [
    path('list/',PictureList.as_view()),
    path('upload/',PictureUpload.as_view()),
    path('detail/<int:pk>/',PictureDetail.as_view()),
]
