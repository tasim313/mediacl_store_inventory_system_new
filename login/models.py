from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,
                                verbose_name='Pharmacy Shop Owner or Pharmacy Super Admin',
                                related_name='pharmacy_admin')
    lic_no = models.CharField(max_length=300, verbose_name='Drug Administration License Number', unique=True)
    s_name = models.CharField(max_length=300, verbose_name='Pharmacy Shop Name')
    name = models.CharField(max_length=264, verbose_name='Full Name')
    contact = models.CharField(max_length=264, verbose_name='Phone Number')
    address = models.CharField(max_length=300, verbose_name="Address")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['lic_no']

    def __str__(self):
        return f'Pharmacy Shop Name: {self.s_name}, Drug Administration License Number: {self.lic_no}'


class Manager(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name='Pharmacy Manager',
                                related_name='manager')
    pharmacy_name = models.CharField(max_length=264, verbose_name='Pharmacy Name')
    name = models.CharField(max_length=264, verbose_name='Full name')
    contact = models.CharField(max_length=264, verbose_name='Phone Number')
    address = models.CharField(max_length=300, verbose_name='Address')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Manager Name: {self.name} {self.pharmacy_name}'


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name='Employee', related_name='employee')
    pharmacy_name = models.CharField(max_length=264, verbose_name='Pharmacy Name')
    name = models.CharField(max_length=264, verbose_name='Full name')
    contact = models.CharField(max_length=264, verbose_name='Phone Number')
    address = models.CharField(max_length=300, verbose_name='Address')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'Employee Name: {self.name} {self.pharmacy_name}'

