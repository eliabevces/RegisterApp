from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib import messages
from django.core.files.storage import default_storage

from RegisterApp.models import User
from RegisterApp.serializers import UserSerializer

from .forms import UserForm,UpdateForm

@csrf_exempt
def list_users(request):
    users = User.objects.all()
    users_serializer = UserSerializer(users, many=True)
    return render(request, 'index.html', {'users': users})

@csrf_exempt
def add_user(request):
    {'success': False }
    form = UserForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Usuário adicionado")
        return redirect(list_users)

    return render(request, 'form.html', {'form': form})


@csrf_exempt
def update_user(request,id=0):
    user = User.objects.get(UserId=id)
    form = UpdateForm(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        messages.info(request, "Usuário Atualizado")
        return redirect(list_users)

    return render(request, 'form.html', {'form': form, 'user': user})


@csrf_exempt
def delete_user(request, id=0):
    user = User.objects.get(UserId=id)

    if request.method == 'POST':
        user.delete()
        messages.warning(request, "Usuário excluido")
        return redirect(list_users)

    return render(request, 'confirm_delete.html', {'user': user})