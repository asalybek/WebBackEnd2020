from django.urls import path
from api.views import product_list, product_detail, category_list, category_detail, products_in_category

urlpatterns = [
    path('products/',product_list),
    path('products/<int:product_id>', product_detail),
    path('categories/', category_list),
    path('categories/<int:category_id>', category_detail),
    path('categories/<int:category_id>/products/', products_in_category),
]