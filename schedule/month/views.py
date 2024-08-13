from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import author  # Make sure to import Author correctly

# Define your month schedule
month_schedule = {
    'january': 'Learning Python',
    'february': 'Learning Django',
    'march': 'Learning AWS',
    'april': 'Learning GIT'
}

def monthly_details_by_number(request, month):
    months = list(month_schedule.keys())
    if month > len(months):
        return HttpResponseNotFound('Enter 1 to 4')
    
    redirect_month = months[month - 1]
    redirect_path = reverse('month-detail', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_details(request, month):
    try:
        month_text = month_schedule[month]
        return HttpResponse(month_text)
    except KeyError:
        return HttpResponseNotFound('No Schedule')

def displaydata(request):
    auth = author.objects.all()
    return render(request, "month/month.html", {
        "authors": auth
    })
