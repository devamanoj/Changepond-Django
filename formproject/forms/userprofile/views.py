from django.shortcuts import render
from django.http import *
from .forms import details
# Create your views here.
def forms(request):
    if request.method == "POST":
        form_data = details(request.POST) # i will get the data from the froms
        print(form_data)
        if form_data.is_valid(): # i it check it is valid are nt inside the html page it self 
            return HttpResponseRedirect("feedback")
    form_data = details() # it will act like the form and we written in the forms.py 
    return render(request,"forms/forms.html", {"data":form_data})

def feedback(request):
    return render(request,"forms/thankyou.html")