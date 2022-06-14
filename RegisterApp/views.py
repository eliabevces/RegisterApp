from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from RegisterApp.models import User
from RegisterApp.serializers import UserSerializer

from django.core.files.storage import default_storage

from .forms import UserForm,UploadFileForm
# from .forms import ModelFormWithFileField



# Create your views here.

# @csrf_exempt
# def userApi(request, id=0):
#     if request.method=='GET':
#         users = User.objects.all()
#         users_serializer = UserSerializer(users, many=True)
#         return render(request, 'index.html', {'users': users})
#     elif request.method=='POST':
#         user_data = JSONParser().parse(request)
#         users_serializer=UserSerializer(data=user_data)
#         if users_serializer.is_valid():
#             users_serializer.save()
#             return JsonResponse("Added Successfully", safe=False)
#         return JsonResponse("Failed to Add", safe=False)
#     elif request.method=='PUT':
#         user_data = JSONParser().parse(request)
#         user=User.objects.get(UserId=user_data['UserId'])
#         users_serializer=UserSerializer(user, data=user_data)
#         if users_serializer.is_valid():
#             users_serializer.save()
#             return JsonResponse("Updated Successfully", safe=False)
#         return JsonResponse("Failed to Update")
#     elif request.method=='DELETE':
#         user=User.objects.get(UserId=id)
#         user.delete()
#         return JsonResponse("Deleted successfully", safe=False)

@csrf_exempt
def list_users(request):
    # if request.method=='GET':
    users = User.objects.all()
    users_serializer = UserSerializer(users, many=True)
    return render(request, 'index.html', {'users': users})

@csrf_exempt
def add_user(request):
    # if request.method=='POST':
    form = UserForm(request.POST or None, request.FILES)

    if form.is_valid():
        form.save()
        return redirect(list_users)

    return render(request, 'form.html', {'form': form})
    # if request.method=='POST':
    #     user_data = JSONParser().parse(request)
    #     users_serializer=UserSerializer(data=user_data)
    #     if users_serializer.is_valid():
    #         users_serializer.save()
    #         return JsonResponse("Added Successfully", safe=False)
    #     return JsonResponse("Failed to Add", safe=False)
    # return render(request, 'form.html')

@csrf_exempt
def update_user(request,id=0):
    # if request.method=='PUT':
    user = User.objects.get(UserId=id)
    form = UserForm(request.POST or None,request.FILES, instance=user)

    if form.is_valid():
        form.save()
        return redirect(list_users)

    return render(request, 'form.html', {'form': form, 'user': user})
    # if request.method=='PUT':
    #     user_data = JSONParser().parse(request)
    #     user=User.objects.get(UserId=id)
    #     users_serializer=UserSerializer(user, data=user_data)
    #     if users_serializer.is_valid():
    #         users_serializer.save()
    #         return JsonResponse("Updated Successfully", safe=False)
    #     return JsonResponse("Failed to Update")

@csrf_exempt
def delete_user(request, id=0):
    # if request.method=='DELETE':
    user = User.objects.get(UserId=id)

    if request.method == 'POST':
        user.delete()
        return redirect(list_users)

    return render(request, 'confirm_delete.html', {'user': user})

    # if request.method=='DELETE':
    #     user=User.objects.get(UserId=id)
    #     user.delete()
    #     return JsonResponse("Deleted successfully", safe=False)


# @csrf_exempt
# def SaveFile(request, id=0):
#     user = User.objects.get(UserId=id)
#     file=request.FILES['ResumeFile']
#     user.ResumeFile = file
#     file_name=default_storage.save(file.name, file)
#     return redirect(list_users)
#     # return JsonResponse(file_name, safe=False)

# @csrf_exempt
# def upload_file(request):
#     if request.method == 'POST':
#         print('é post')
#         form = UploadFileForm(request.POST)
#         # file = request.FILES['ResumeFile']
#         if form.is_valid():
#             # instance = User(file_field=request.FILES['ResumeFile'])
#             print('is valid')
#             form.save()
#             return redirect(list_users)
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})