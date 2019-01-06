"""Users views.
"""

from django.shortcuts import render
from django.contrib.auth import authenticate, login

def login_view(request):
    """Login view.
    
    Arguments:
        request {[type]} -- [description]
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print (username, password)
    return render(request, 'users/login.html')



