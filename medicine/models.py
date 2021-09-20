from django.db import models

from login.models import Admin, Manager, Employee, CustomUser
# Create your models here.


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Company Name')
    lic_no = models.CharField(max_length=300, verbose_name='License Number')
    address = models.CharField(max_length=300, verbose_name='Company Headquarter Address')
    cont_num = models.CharField(max_length=264, verbose_name='Company Contact Information')
    email = models.EmailField()
    description = models.CharField(max_length=300, verbose_name='Company Description')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'Company Name:{self.name};Company Address:{self.address}'


class MedicineProduct(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Serial Number')
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_medicine', null=True, blank=True)
    name = models.CharField(max_length=300, verbose_name='Medicine Name', null=True)
    m_type = models.CharField(max_length=300, verbose_name='Which type of Medicine', null=True)
    des = models.CharField(max_length=500, verbose_name='Medicine Description', null=True)
    b_no = models.CharField(max_length=100, verbose_name='Batch No', null=True)
    s_no = models.CharField(max_length=100, verbose_name='Shelf No or Rack No', null=True)
    mfg_date = models.DateField(verbose_name='Manufacture Date')
    expire_date = models.DateField(verbose_name='Expire Date')
    dar_no = models.CharField(max_length=300, verbose_name='Combination of Drag Administration Number', null=True)
    mfg_Lic = models.CharField(max_length=300, verbose_name='Manufacturing Licence Number', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_quantity = models.IntegerField(default=0, null=True, blank=True)
    issued_quantity = models.IntegerField(default=0, null=True, blank=True)
    received_quantity = models.IntegerField(default=0, null=True, blank=True)
    buy_price = models.IntegerField(default=0, null=True, blank=True)
    unit_price = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'Medicine Name:{self.name};Medicine Type:{self.m_type}'


class Sale(models.Model):
    item = models.ForeignKey(MedicineProduct, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    amount_received = models.IntegerField(default=0, null=True, blank=True)
    unit_price = models.IntegerField(default=0, null=True, blank=True)
    issued_to = models.CharField(max_length=50, null=True, blank=True, verbose_name='Issued To')

    def get_total(self):
        total = self.quantity * self.item.unit_price
        return int(total)

    def get_change(self):
        change = self.get_total() - self.amount_received
        return abs(int(change))

    def get_profit(self):
        total = self.unit_price - self.item.buy_price
        return int(total)

    def __str__(self):
        return self.item.name
