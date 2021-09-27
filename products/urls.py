from django.urls import path

from .views import *

app_name = "products"
urlpatterns = [
    path('product/', product_details_view, name="prd_det_view"),
    path('product_create', product_create_view, name="prd_create_view"),
    path('product_create2', product_create_raw_view, name="prd_create_view2"),
    path('product/<int:pid>/', product_dynamic_lookup_view, name="prd_lookup"),
    path('product/<int:pid>/delete/', product_delete_view, name="prd_delete"),
    path('products', product_list_view, name="prd_list")
]
