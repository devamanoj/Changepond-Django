from django.urls import path
from . import views
urlpatterns = [
    path("profile_upload", views.image_upload)
]
