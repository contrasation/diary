from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def regist_data(request):
    return HttpResponse('Jesus Kingdom!')

def today(request):
    message = 'Today\'s schedule is'

    d = {
        'message': message,
    }
    return render(request, 'today.html', d)

def get_query(request):
    # d = {
    #     'subject': request.POST('subject'),
    #     'content': request.POST('content'),
    # }
    if request.POST.get('subject') is not None \
            or request.POST.get('content') is not None:
        d = {
            'subject': request.POST.get('subject'),
            'content': request.POST.get('content'),
        }
    else:
        d = {}

    return render(request, 'get_query.html', d)


def index(request):
    if datetime.now().hour in range(18, 23) \
        or datetime.now().hour in range(0,6):
        message = 'Good Evening!'
    elif datetime.now().hour in range(7,11):
        message = 'Good Morning!'
    else:
        message = 'Good Afternoon!'

    d = {
        'hour': datetime.now().hour,
        'minute': datetime.now().minute,
        'message': message,
    }
    return render(request, 'index.html', d)
