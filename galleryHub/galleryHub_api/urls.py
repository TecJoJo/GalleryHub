
from django.contrib import admin
from django.urls import path
from galleryHub_api.views import pictureList, picture_upload, picture_detail


urlpatterns = [
    path('list/',pictureList),
    path('upload/',picture_upload),
    path('detail/<int:pk>',picture_detail)
]
