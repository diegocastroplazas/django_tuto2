""""Platzigram views"""

#Django
from django.http import HttpResponse
#Utilites
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now()
    return HttpResponse("Current server time is: {now}".format(
        now=now.strftime('%Y-%m-%dth T %H:%M')
    ))

def hi(request):
    #import pdb; pdb.set_trace()
    numbers = request.GET['numbers']
    numbers = [int(i) for i in numbers.split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application/json'
    )

def say_hi(request, name, age):
    """Return a greeting"""
    if (age < 12):
        message = 'Sorry {}, you are not allowed here'. format(str(name))
    else:
        message = 'Hello, {}, welcome to Platzi'.format(str(name))
    return HttpResponse(
        message
    )