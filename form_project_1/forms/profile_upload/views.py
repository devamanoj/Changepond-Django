from django.shortcuts import render

# Create your views here.

def image_upload(request):
    return render(request,"profile_upload/form_profile.html")