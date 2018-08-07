from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from .models import Product, ProductCategory


class ProductCategoryListView(generic.ListView):
    template_name = 'shop/product_category_list.html'
    context_object_name = 'product_category_list'

    def get_queryset(self):
        """
        Возвращает существующие категории товаров
        :return: 
        """
        return ProductCategory.objects.order_by('name')


class ProductListView(generic.ListView):
    context_object_name = 'product_list'

    def get_queryset(self):
        """
        Возвращает продукты выбранной категории
        :return: 
        """
        return Product.objects.filter(
            category=self.kwargs['pk']
        ).order_by('-create_date')


class ProductDetailView(generic.DetailView):
    model = Product

