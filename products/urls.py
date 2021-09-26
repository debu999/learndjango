from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('product/', product_details_view, name="prd_det_view"),
    path('product_create', product_create_view, name="prd_create_view"),
    path('product_create2', product_create_raw_view, name="prd_create_view2"),
    path('product/<int:pid>/', product_dynamic_lookup_view, name="prd_lookup"),
    path('product/<int:pid>/delete/', product_delete_view, name="prd_delete")
]
