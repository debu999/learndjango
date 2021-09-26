from django.urls import re_path, path

from .views import *

urlpatterns = [

    re_path(r'^$', home_view, name="p_home"),
    path(r'contacts', contact_view, name="p_contact"),
    path(r'about', about_view, name="p_about"),
    path(r'developer', developer_view, name="p_developer"),
]
