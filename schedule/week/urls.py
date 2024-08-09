from django.urls import path
from . import views

urlpatterns = [
    path('<int:day_number>/', views.weekly_details_by_number, name='week-details-by-number'),
    path('day/<str:day>/', views.weekly_details, name='week-detail'),
]
