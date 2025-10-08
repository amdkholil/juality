from django.db import models
from akun.models import Tenant, UserProfile


class Product(models.Model):
    tenant = models.ForeignKey(
        Tenant, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name + ' - ' + str(self.price)


class Transaction(models.Model):
    tenant = models.ForeignKey(
        Tenant, on_delete=models.CASCADE, related_name='transactions')
    total_price = models.IntegerField(default=0)
    type_transaction = models.CharField(max_length=20, choices=[
        ('in', 'In'),
        ('out', 'Out'),
    ])
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='transactions',
    )

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        return self.product.name


class TransactinItem(models.Model):
    product = models.ForeignKey(
        Product, null=True, blank=True, on_delete=models.CASCADE, related_name='transaction_items')
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(null=True, blank=True)
