from django.shortcuts import render
from .models import Posts
# Create your views here.



def Home(request):
    # posts_data = Posts.objects.all().order_by("-time").values()[0:3]
    posts_data = Posts.objects.all().order_by("time")[0:3]
    # post_data = posts_data[-3:]
    return render(request, "deva_app/home.html",{"data":posts_data,"d":""})
def details(request,pk):
    posts_details = Posts.objects.get(pk=pk)
    return render(request,"deva_app/all.html",{"post":posts_details})

def all_details(request):
    return render(request,"deva_app/details.html",{"data":Posts.objects.all()})