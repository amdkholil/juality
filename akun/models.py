from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    class Meta:
        verbose_name = 'Tenant'
        verbose_name_plural = 'Tenants'

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(
        'auth.User', on_delete=models.CASCADE, related_name='profile')
    tenant = models.ForeignKey(Tenant, on_delete=models.SET_NULL, null=True)
    role = models.CharField(
        max_length=100,
        choices=[
            ('owner', 'Owner'),
            ('kasir', 'Kasir'),
            ('helper', 'Helper'),
        ]
    )
    image = models.ImageField(
        upload_to='profile_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.user.username
