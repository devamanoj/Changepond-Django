from django.shortcuts import render
from .forms import *
# from django.views import View
# from django.http import *
from .models import profile1
# Create your views here.

# # this ste
# def storefile(file):
#     with open("temp/image.jpg","+wb") as files:
#         for trash in file.chunks():
#             files.write(trash)
            

# class UserImageView(View):
#     def get(self,request):
#         form = profile()
        
#         return render(request,"profile_upload/form_profile.html",
#                       {"form":form}
#                       )
#     def post(self,request):
#         form = profile(request.POST,request.FILES)
#         if form.is_valid():
#             storefile(request.FILES["image"])
#             return HttpResponseRedirect("/profile")
#         return render(request,"profile_upload/form_profile.html",{"form":form})

# def image_upload(request):
#     return render(request,"profile_upload/form_profile.html")

from django.views.generic.edit import CreateView
class CreateProfileView(CreateView):
    model = profile1
    template_name = "profile_upload/form_profile.html"
    success_url ='/profile'
    fields ="__all__"