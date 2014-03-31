from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from rest_framework import authtoken
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, render
from models import File
from django.core import serializers
from django.shortcuts import redirect
from django.core.files import File
import urllib

import json
# Create your views here.

def OneDir(request):
    return HttpResponse("Welcome to OneDir, Beta coming soon!")


# @csrf_exempt
# def GetFiles(request, user):
#     response_data = {}
#     response_data['user']= user
#     return HttpResponse(json.dumps(response_data), content_type="application/json")

#file prefix needs to be changed below to mactch the machine running DJServer

@api_view(['POST'])
@csrf_exempt
def UploadFile(request):
    uFile = File(request.FILES['file'])
    uname = request.user.username
    with open('/home/hodor/OneDir/OneDir/Server/Files/' + uname+'/' + uFile.name, 'w+') as destination:
        for chunk in uFile.chunks():
            destination.write(chunk)
    return HttpResponse('successful upload')


@api_view(['GET'])
@csrf_exempt
def GetFile(request, user, filename):
    return redirect('http://127.0.0.1:8000/Serve/'+user+'/'+filename)

@api_view(['GET'])
@csrf_exempt
def ListFiles(request, user):
    if not request.user.is_authenticated():
        return HttpResponse('Unauthorized')
    query = File.objects.filter(name__username = user)
    user_files = query.values_list('fileName', 'id')
    newList = {}
    for s in user_files:
        newList[s[1]] = s[0]
    return HttpResponse(json.dumps(newList), content_type="application/json")

@api_view(['GET'])
@csrf_exempt
def LoggedIn(request):
    if request.user.is_authenticated():
        return HttpResponse("User is currently logged in. User = " + request.user.username)
    else:
        return HttpResponse("User is NOT currently logged in.")
