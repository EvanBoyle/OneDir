from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def OneDir(request):
    return HttpResponse("Welcome to OneDir, Beta coming soon!")
@csrf_exempt
def GetFiles(request, user=None):
    response_data = {}
    response_data['user']= user
    return HttpResponse(json.dumps(response_data), content_type="application/json")
@csrf_exempt
def AuthTest(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Return a success message
            return HttpResponse("Login successful!")

        else:
            # Return a 'disabled account' error message
            return HttpResponse("Account is disabled.")
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("invalid login.")
@csrf_exempt
def Get_Login(request):
    if request.user.is_authenticated():
        return HttpResponse("User is currently logged in.")
    else:
        return HttpResponse("User is NOT currently logged in.")
