
from django.contrib import admin
from django.urls import path
from galleryHub_api.views import pictureList, picture_upload


urlpatterns = [
    path('list/',pictureList),
    path('upload/',picture_upload)
]
