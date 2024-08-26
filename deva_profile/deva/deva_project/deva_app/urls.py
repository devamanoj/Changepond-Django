from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home ),
    path("all_link", views.all_details, name="all"),
    path("forms", views.FormViews.as_view(), name="forms"),
    path("<int:pk>", views.details, name="details-link")
]
