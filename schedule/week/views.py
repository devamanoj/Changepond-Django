from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Define the week schedule
week_schedule = {
    'monday': 'Learning Python Basics',
    'tuesday': 'Learning Django Basics',
    'wednesday': 'Learning AWS Basics',
    'thursday': 'Learning Git Basics',
    'friday': 'Project Work',
    'saturday': 'Review and Practice',
    'sunday': 'Rest Day'
}

def weekly_details_by_number(request, day_number):
    weekdays = list(week_schedule.keys())
    if day_number < 1 or day_number > len(weekdays):
        return HttpResponseNotFound('Enter a number between 1 and 7')
    redirect_day = weekdays[day_number - 1]
    redirect_path = reverse('week-detail', args=[redirect_day])
    print(redirect_path)
    return HttpResponseRedirect(redirect_path)

def weekly_details(request, day):
    try:
        day_text = week_schedule[day]
        return HttpResponse(day_text)
    except KeyError:
        return HttpResponseNotFound('No Schedule')
