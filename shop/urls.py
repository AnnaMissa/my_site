from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.ProductCategoryListView.as_view(), name='product_category_list'),
    path('category_<int:pk>/', views.ProductListView.as_view(), name='product_list'),
    path('product_<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]
