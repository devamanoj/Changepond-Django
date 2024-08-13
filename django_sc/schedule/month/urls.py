from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path("",views.index),
    path("<int:month>",views.month_in_number),
    path("<str:month>",views.month_details, name = "month-detail" ),
    
]