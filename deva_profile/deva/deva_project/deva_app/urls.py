from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home ),
    path("all_link", views.all_details, name="all"),
    path("<int:pk>", views.details, name="details-link")
]
