from django.urls import path
from . import views

urlpatterns = [
    path('', views.author_list, name='author_list'),
    path('<int:id>/', views.author_detail, name='author_detail'),
    path('<str:slug>/', views.slugs, name='author_detail'),
]
