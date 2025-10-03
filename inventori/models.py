from django.db import models


class Product(models.Model):
    tenant = models.ForeignKey(
        'akun.Tenant', on_delete=models.CASCADE, related_name='products')
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


class Package(models.Model):
    tenant = models.ForeignKey(
        'akun.Tenant', on_delete=models.CASCADE, related_name='packages')
    products = models.foreignKey(
        'inventori.Product', related_name='packages')
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    qty = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Package'
        verbose_name_plural = 'Packages'

    def __str__(self):
        return self.name + ' - ' + str(self.price)


class Transaction(models.Model):
    tenant = models.ForeignKey(
        'akun.Tenant', on_delete=models.CASCADE, related_name='transactions')
    product = models.ForeignKey(
        'inventori.Product', null=True, blank=True, on_delete=models.CASCADE, related_name='transactions')
    package = models.ForeignKey(
        'inventori.Package', null=True, blank=True, on_delete=models.CASCADE, related_name='transactions'
    )
    is_package = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    type_transaction = models.CharField(max_length=20, choices=[
        ('in', 'In'),
        ('out', 'Out'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        'akun.UserProfile',
        on_delete=models.SET_NULL,
        null=True,
        related_name='transactions',
    )

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        return self.product.name
