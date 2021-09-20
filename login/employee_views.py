from django.shortcuts import render, redirect
from .models import Employee

from django.views.generic import CreateView

from .decorators import employee_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from medicine.models import Company, MedicineProduct, Sale


@method_decorator([login_required, employee_required], name='dispatch')
class EmployeeProfile(CreateView):
    model = Employee
    template_name = 'Employee/profile.html'
    fields = ('pharmacy_name', 'name', 'contact', 'address')

    def form_valid(self, form):
        employee_obj = form.save(commit=False)
        employee_obj.user = self.request.user
        employee_obj.save()
        messages.success(self.request, 'The profile was created with success! ')
        return redirect('App_Login:employee_main_home')


def index(request):
    return render(request, 'Employee/employee_home_page.html')


@login_required
def employee_dashboard(request):
    meadicine = MedicineProduct.objects.all()
    medicine_count = meadicine.count()
    company = Company.objects.all()
    company_count = company.count()
    sales = Sale.objects.all()
    profit = sum([items.get_profit() for items in sales])
    diction = {
        'medicine_count': medicine_count,
        'profit': profit, 'company_count': company_count,
    }
    return render(request, 'Employee/employee_main_homepage.html', context=diction)
