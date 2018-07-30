from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from .models import Product


class ProductListView(generic.ListView):
    context_object_name = 'new_product_list'

    def get_queryset(self):
        """
        Возвращает последние пять созданных товаров
        :return: 
        """
        return Product.objects.filter(
            create_date__lte=timezone.now()
        ).order_by('-create_date')[:5]


class ProductDetailView(generic.DetailView):
    model = Product
