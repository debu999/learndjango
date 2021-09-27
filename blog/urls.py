from django.urls import path

from .views import *

app_name = "articles"
urlpatterns = [
    path('', ArticleListView.as_view(), name="article_list"),
    path('<int:id>/', ArticleDetailView.as_view(), name="article_lookup"),
    path('create/', ArticleCreateView.as_view(), name="article_create_view"),
    # path('product_create2', product_create_raw_view, name="prd_create_view2"),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name="article_update_view"),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name="article_delete_view"),
    # path('products', product_list_view, name="prd_list")
]
