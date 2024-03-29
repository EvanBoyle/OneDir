from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from models import ODFile
from django.shortcuts import redirect
from django.core.files import File
import hashlib
import os
from django.core.serializers.json import DjangoJSONEncoder
import sys
import constants
import json
import logging
import shutil
# Create your views here.

logger = logging.getLogger('ActionLog')

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
    #manipulating the header to get vars
    uFile = File(request.FILES['file'])
    uname = request.user.username
    path = request.DATA['path']

    #logging
    logDict = {}
    logDict['User']= request.user.username
    logDict['Action']= 'UploadFile'
    logDict['HTTP']= 'POST'
    logDict['File']= request.DATA['path']+uFile.name;
    logger.info(json.dumps(logDict))

    #deleting obj in db
    query = ODFile.objects.filter(name=request.user, fileName = path+uFile.name).delete()

    #writing file and creating md5 hash
    md5 = hashlib.md5()
    if not os.path.exists('../Server/Files/'+ uname + '/'+ path):
        os.makedirs('../Server/Files/'+ uname + '/'+ path)
    with open('../Server/Files/' + uname+'/'+path+ uFile.name, 'w+') as destination:
        for chunk in uFile.chunks():
            md5.update(chunk)
            destination.write(chunk)
    f = ODFile(fileName=path+ uFile.name.decode("utf-8"), name = request.user, fileHash=md5.hexdigest().decode("utf-8"), fileSize=uFile.size)
    f.save()
    return HttpResponse(constants.h_uploadFile_success)

@api_view(['DELETE'])
@csrf_exempt
def DeleteUser(request, user):
    if request.user.is_superuser:
        logDict = {}
        logDict['User']= request.user.username
        logDict['Action']= 'DeleteUser'
        logDict['HTTP']= 'DELETE'
        logDict['File']= 'N/A'
        logger.info(json.dumps(logDict))
        if os.path.exists('../Server/Files/'+user):
            shutil.rmtree('../Server/Files/'+user)
        target = User.objects.filter(username=user).first()
        query = ODFile.objects.filter(name=target).delete()
        query = User.objects.filter(username=user).delete()

        return HttpResponse(constants.h_deleteUser_success)
    else:
        return HttpResponse(constants.h_deleteUser_fail)

@api_view(['DELETE'])
@csrf_exempt
def DeleteFile(request, user, filename):
    logDict = {}
    logDict['User']= request.user.username
    logDict['Action']= 'DeleteFile'
    logDict['HTTP']= 'DELETE'
    logDict['File']= filename
    logger.info(json.dumps(logDict))

    print '../Server/Files/'+user+'/'+filename
    if os.path.isfile('../Server/Files/'+user+'/'+filename):
        os.remove('../Server/Files/'+user+'/'+filename)
        query = ODFile.objects.filter(name=request.user, fileName =filename).delete()
        return HttpResponse(constants.h_deleteFile_success)
    else:
        return HttpResponse(constants.h_deleteFile_fail)

@api_view(['GET'])
@csrf_exempt
def GetFile(request, user, filename):
    logDict = {}
    logDict['User']= request.user.username
    logDict['Action']= 'GetFile'
    logDict['HTTP']= 'GET'
    logDict['File']= filename
    logger.info(json.dumps(logDict))

    return redirect(constants.server_url + '/Serve/'+user+'/'+filename)

@api_view(['GET'])
@csrf_exempt
def ListFiles(request, user):
    logDict = {}
    logDict['User']= request.user.username
    logDict['Action']= 'ListFiles'
    logDict['HTTP']= 'GET'
    logDict['File']= 'N/A'
    logger.info(json.dumps(logDict))


    if not request.user.is_authenticated():
        return HttpResponse(constants.h_listFiles_fail)
    query = ODFile.objects.filter(name__username = user)
    user_files = query.values_list('fileName', 'fileSize', 'fileHash', 'timestamp' )
    newList = {}
    for s in user_files:
        newList[s[0]]= user_files
    return HttpResponse(json.dumps(list(user_files), cls=DjangoJSONEncoder), content_type="application/json")

@api_view(['GET'])
@csrf_exempt
def LoggedIn(request):
    logDict = {}
    logDict['User']= request.user.username
    logDict['Action']= 'LoggedIn'
    logDict['HTTP']= 'GET'
    logDict['File']= 'N/A';
    logger.info(json.dumps(logDict))

    if request.user.is_authenticated():
        return HttpResponse(constants.h_loggedIn_true + ' User = ' + request.user.username)
    else:
        return HttpResponse(constants.h_loggedIn_false)


@csrf_exempt
def CreateUser(request):
    logDict = {}
    logDict['User']= 'N/A'
    logDict['Action']= 'CreateUser'
    logDict['HTTP']= 'POST'
    logDict['File']= 'N/A';
    logger.info(json.dumps(logDict))
    un = request.POST['username']
    email = request.POST['email']
    pw = request.POST['password']
    User.objects.create_user(un, email, pw).save()
    return HttpResponse(constants.h_createUser_success)

@api_view(['POST'])
@csrf_exempt
def ChangePassword(request):
    logDict = {}
    logDict['User']= request.user.username
    logDict['Action']= 'ChangePasswords'
    logDict['HTTP']= 'POST'
    logDict['File']= 'N/A'
    logger.info(json.dumps(logDict))
    oldpw = request.POST['oldPass']
    newpw = request.POST['newPass']
    if request.user.check_password(oldpw):
        request.user.set_password(newpw)
        request.user.save()
        return HttpResponse(constants.h_changePassword_success)
    return HttpResponse(constants.h_changePassword_fail)
