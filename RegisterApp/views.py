from dataclasses import dataclass
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from numpy import delete, safe_eval
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from RegisterApp.models import User
from RegisterApp.serializers import UserSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def userApi(request, id=0):
    if request.method=='GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method=='POST':
        user_data = JSONParser().parse(request)
        users_serializer=UserSerializer(data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        user_data = JSONParser().parse(request)
        user=User.objects.get(UserId=user_data['UserId'])
        users_serializer=UserSerializer(user, data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        user=User.objects.get(UserId=id)
        user.delete()
        return JsonResponse("Deleted successfully", safe=False)


@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)