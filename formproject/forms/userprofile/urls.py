from django.urls import path
from . import views
urlpatterns = [
    path("forma",views.forms),
    path("feedback",views.feedback)
]
