"""oauth2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path

from oauth2 import views as v

urlpatterns = [
    re_path(r'^$', v.home, name="home"),
    path('login', v.discord_login, name="login"),
    path('login/redirect', v.discord_redirect, name="login_redirect"),
    path('user', v.get_authenticated_user, name="get_authenticated_user"),
    path('register', v.RegisterView.as_view(), name="register"),
    path('lgn', v.LoginView.as_view(), name="lgn"),
    path("usr", v.UserView.as_view(), name="usr"),
    path('logout', v.LogoutView.as_view(), name="logout")
]
