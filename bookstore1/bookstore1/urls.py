"""bookstore1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#  from django.contrib import admin
#  from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
# from django.contrib import admin
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Set up the schema view for Swagger and ReDoc
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Book store API documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="sandeep003.mnmn@gmail.com"),  # Corrected here
      license=openapi.License(name="BSD License"),
   ),
   public=True,
#    permission_classes=(permissions.AllowAny,),
)

# Define the URL patterns
urlpatterns = [
   path('admin/', admin.site.urls),  # Include the admin URLs
#    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),  # Swagger JSON and YAML format
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
#    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
#   # ReDoc UI
   path("api/author/",include('authorapp.urls')),
]
