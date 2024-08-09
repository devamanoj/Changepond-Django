from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect

# Create your views here.

month_schedule = {
    'january'  : 'Learning Python',
    'febraury' : 'Learning Django',
    'march' :   'Leaning AWS',
    'april' :   'Learning GIT'
}
def monthly_details_by_number(request,month):
    #return HttpResponse(month)

    months = list(month_schedule.keys())
    if(month>len(months)):
        return HttpResponseNotFound('Enter 1 to 4')
    redirect_month = months[month-1]
    redirect_path = reverse('month-detail',args=[redirect_month])
    print(redirect_path)
    # return HttpResponseRedirect('/month/'+redirect_month)
    return HttpResponseRedirect(redirect_path)

def monthly_details(request,month):
    try:
        month_text = month_schedule[month]
        return HttpResponse(month_text)
    except:
        return HttpResponseNotFound('No Schedule')