from django.db import models


class ProductCategory(models.Model):
    """
    Модель категории товара
    """
    name = models.CharField(max_length=100)
    create_date = models.DateField(auto_now_add=True)
    write_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Модель товара
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)
    create_date = models.DateField(auto_now_add=True)
    write_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
