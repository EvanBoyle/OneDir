from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def OneDir(request):
    return HttpResponse("Welcome to OneDir, Beta coming soon!")

def GetFiles(request, user=None):
    response_data = {}
    response_data['user']= user
    return HttpResponse(json.dumps(response_data), content_type="application/json")
