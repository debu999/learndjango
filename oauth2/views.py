import logging
from datetime import datetime, timedelta

import jwt
import requests
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponseRedirect
# Create your views here.
from django.shortcuts import redirect
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from oauth2.models import User
from oauth2.serializers import UserSerializer

logger = logging.getLogger(__name__)

auth_url_discord = "https://discord.com/api/oauth2/authorize?client_id=884012002463346689" \
                   "&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Foauth2%2Flogin%2Fredirect" \
                   "&response_type=code&scope=identify"


def home(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"home": "Welcome to Oauth2"})


@login_required(login_url="/oauth2/login")
def get_authenticated_user(request: HttpRequest) -> HttpResponse:
    logger.info({"user": serialize('json', [request.user, ], ensure_ascii=False)[1:-1]})
    return redirect('admin:index')


def discord_login(request: HttpRequest) -> HttpResponseRedirect:
    return redirect(auth_url_discord)


def discord_redirect(request: HttpRequest) -> HttpResponse:
    code = request.GET.get('code')
    logger.info("code: " + code)
    res = get_exchange_code(code=code)
    user = get_usr_info(res.get("access_token"))
    users = list(authenticate(request, user=user))
    login(request, users[0])
    return redirect("/oauth2/user")


def get_exchange_code(code: str) -> dict:
    data = {
        "client_id": "884012002463346689",
        "client_secret": "EeKXc-ccFBlUC2w58fCIeqMiNExElPOg",
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://localhost:8000/oauth2/login/redirect",
        "scope": "identify"
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post("https://discord.com/api/oauth2/token", data=data, headers=headers)
    return response.json()


def get_usr_info(token: str) -> dict:
    res = requests.get("https://discord.com/api/v6/users/@me",
                       headers={"Authorization": "Bearer " + token})
    logger.info(res.json())
    user = res.json()
    return user


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = User.objects.filter(email=email).first()

        if user is None or not user.check_password(password):
            raise AuthenticationFailed('User not Found/Incorrect Password.')

        payload = {
            'id': user.id,
            'exp': datetime.utcnow() + timedelta(minutes=60),
            'iat': datetime.utcnow()
        }
        token = jwt.encode(payload=payload, key="secret")
        response = Response()
        response.set_cookie(key="jwt", value=token, httponly=True)
        response.data = {"mesage": "success"}
        return response


class UserView(APIView):
    def get(self, request):
        tok = request.COOKIES.get("jwt")

        if not tok:
            raise AuthenticationFailed("Unauthenticated")
        try:
            payload = jwt.decode(tok, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthorized")
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        response = Response()
        response.data = {"user": serializer.data}
        return response


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie("jwt")
        response.data = {"message": "You have been logged out successfully."}
        return response
