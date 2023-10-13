import hashlib
import os

from django.http import JsonResponse
from django.views import View
from main.models import Users
from main.settings.functions import get_client_ip


# Выход из аккаунта через ajax
class LogoutProc(View):
    def post(self, request):
        try:
            del request.session['id']
            del request.session['email']
            del request.session['token']
            return JsonResponse(data={}, status=200)
        except KeyError:
            return JsonResponse(data={}, status=400)


# Авторизация через ajax
class LoginProc(View):
    async def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            user = Users.objects.get(email=email)
            if user:
                tmp = await hashlib.pbkdf2_hmac('sha256', str(password).encode('utf-8'), user.salt, 100000)
                if tmp == user.key:
                    token = os.urandom(16)
                    request.session['id'] = user.id
                    request.session['email'] = user.email
                    request.session['token'] = token
                    Users.objects.filter(id=user.id).update(ip=get_client_ip(request), session=token)
                    return JsonResponse(data={}, status=200)
        return JsonResponse(data={}, status=400)


# Регистрация через ajax
class RegisterProc(View):
    async def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if name and email and password:
            salt = os.urandom(32)
            key = await hashlib.pbkdf2_hmac('sha256', str(password).encode('utf-8'), salt, 100000)
            create = Users(email=email, password=key, salt=salt, name=name, code=os.urandom(16))
            create.save()
            return JsonResponse(data={}, status=200)
        else:
            return JsonResponse(data={}, status=400)
