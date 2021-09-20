from django import forms

from medicine.models import MedicineProduct, Sale


class AddForm(forms.ModelForm):
    class Meta:
        model = MedicineProduct
        fields = ['received_quantity']


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ('quantity', 'amount_received', 'issued_to',)


class ManagerSaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ('quantity', 'amount_received', 'issued_to',)


class EmployeeSaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ('quantity', 'amount_received', 'issued_to',)
