from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from rest_framework import authtoken
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, render
from models import ODFile
from django.core import serializers
from django.shortcuts import redirect
from django.core.files import File
import urllib
import hashlib
import datetime
import os
from django.core.serializers.json import DjangoJSONEncoder
import constants
import json
# Create your views here.

def OneDir(request):
    return HttpResponse(constants.h_welcome_beta)


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
    path = request.DATA['path'];
    query = ODFile.objects.filter(name=request.user, fileName = path+uFile.name).delete()

    md5 = hashlib.md5()
    if not os.path.exists('/home/hodor/OneDir/OneDir/Server/Files/'+ uname + '/'+ path):
        os.makedirs('/home/hodor/OneDir/OneDir/Server/Files/'+ uname + '/'+ path)
    with open('/home/hodor/OneDir/OneDir/Server/Files/' + uname+'/'+path+ uFile.name, 'w+') as destination:
        for chunk in uFile.chunks():
            md5.update(chunk)
            destination.write(chunk)
    f = ODFile(fileName=path+ uFile.name.decode("utf-8"), name = request.user, fileHash=md5.hexdigest().decode("utf-8"), fileSize=uFile.size)
    f.save()
    return HttpResponse(constants.h_uploadFile_success)


@api_view(['GET'])
@csrf_exempt
def GetFile(request, user, filename):
    return redirect(constants.sever_url + '/Serve/'+user+'/'+filename)

@api_view(['GET'])
@csrf_exempt
def ListFiles(request, user):
    if not request.user.is_authenticated():
        return HttpResponse('Unauthorized')
    query = ODFile.objects.filter(name__username = user)
    user_files = query.values_list('fileName', 'fileSize', 'fileHash', 'timestamp' )
    newList = {}
    for s in user_files:
        newList[s[0]]= user_files
    return HttpResponse(json.dumps(list(user_files), cls=DjangoJSONEncoder), content_type="application/json")

@api_view(['GET'])
@csrf_exempt
def LoggedIn(request):
    if request.user.is_authenticated():
        return HttpResponse(constants.h_loggedIn_true + ' User = ' + request.user.username)
    else:
        return HttpResponse(constants.h_loggedIn_false)

@csrf_exempt
def CreateUser(request):
    # form = UserCreationForm(request.POST)
    # if form.is_valid():
    #     form.save()
    #     return HttpResponse('User has been created.')
    # return HttpResponse('User creation failed.')
    un = request.POST['username']
    email = request.POST['email']
    pw = request.POST['password']
    User.objects.create_user(un, email, pw).save()
    return HttpResponse(constants.h_createUser_success)

@api_view(['POST'])
@csrf_exempt
def ChangePassword(request):
    oldpw = request.POST['oldPass']
    newpw = request.POST['newPass']
    if request.user.check_password(oldpw):
        request.user.set_password(newpw)
        request.user.save()
        return HttpResponse(constants.h_changePassword_success)
    return HttpResponse(constants.h_changePassword_fail)
