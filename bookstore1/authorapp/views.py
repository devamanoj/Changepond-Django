from django.shortcuts import render
from .models import Author
from .serializers import AuthorSerializer,AuthorDetailSerializer,AuthorImageSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status,parsers
from rest_framework.decorators import action
# Create your views here.
class AuthorViewset(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    parser_classes = (parsers.FormParser,parsers.MultiPartParser,parsers.FileUploadParser)
 
    def get_serializer_class(self):
        if self.action == 'list':
            return AuthorSerializer
        elif self.action == 'create':
            return AuthorSerializer
        elif self.action == 'upload_image':
            return AuthorImageSerializer
        return self.serializer_class
 
    @action(methods=['POST'],detail=True,url_path='upload-image')
    def upload_image(self,request,pk=None):
        author_objs =self.get_object()
        serializer=self.get_serializer(author_objs,data=request.data)
        if not serializer.is_valid():
            return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data':serializer.errors,
                    'message':'Inavlid Data'
                })
        serializer.save()
        return Response({
                    'status': status.HTTP_200_OK,
                    'data':serializer.data,
                    'message': 'Author Image Successfully'
                })
 