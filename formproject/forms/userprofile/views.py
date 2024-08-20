from django.shortcuts import render
from django.http import *
from .forms import details
# from .models import Review
# Create your views here.
def forms(request):
    if request.method == "POST":
        form_data = details(request.POST) # i will get the data from the froms
        if form_data.is_valid(): # i it check it is valid are nt inside the html page it self 
            # datas = Review(
            #     user_name = form_data.cleaned_data["user_name_2"],
            #     review = form_data.cleaned_data["rating"],
            #     message = form_data.cleaned_data["message"]
            # )
            # datas.save()
            form_data.save()
            return HttpResponseRedirect("feedback")
    else:
    
        
        form_data = details() # it will act like the form and we written in the forms.py 
    return render(request,"forms/forms.html", {"form":form_data})

def feedback(request):
    return render(request,"forms/thankyou.html")