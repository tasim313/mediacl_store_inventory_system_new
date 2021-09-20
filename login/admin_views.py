from django.shortcuts import render, redirect
from .models import Admin, Employee, Manager

from django.views.generic import CreateView

from .decorators import admin_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from medicine.models import Company, MedicineProduct, Sale


@method_decorator([login_required, admin_required], name='dispatch')
class Profile(CreateView):
    model = Admin
    template_name = 'Admin/profile.html'
    fields = ('lic_no', 's_name', 'name', 'contact', 'address')

    def form_valid(self, form):
        admin_obj = form.save(commit=False)
        admin_obj.user = self.request.user
        admin_obj.save()
        messages.success(self.request, 'The profile was created with success! ')
        return redirect('App_Login:admin_main_home')


def index(request):
    return render(request, 'Admin/HomePage.html')


@login_required
def employee_view(request):
    employee = Employee.objects.all()
    employee_obj = employee.count()
    diction = {'employee': employee, 'employee_obj': employee_obj}
    return render(request, 'Admin/employee_view.html', context=diction)


@login_required
def manager_view(request):
    manager = Manager.objects.all()
    manager_obj = manager.count()
    diction = {'manager': manager, 'manager_obj': manager_obj}
    return render(request, 'Admin/manager_view.html', context=diction)


@login_required
def admin_dashboard(request):
    admin_obj = Admin.objects.get(user=request.user.id)
    employee_count = Employee.objects.all()
    emp_count = employee_count.count()
    manager = Manager.objects.all()
    manager_count = manager.count()
    meadicine = MedicineProduct.objects.all()
    medicine_count = meadicine.count()
    company = Company.objects.all()
    company_count = company.count()
    sales = Sale.objects.all()
    profit = sum([items.get_profit() for items in sales])
    diction = {
        'emp_count': emp_count, 'manager_count': manager_count, 'medicine_count': medicine_count,
        'profit': profit, 'company_count': company_count,
    }
    return render(request, 'Admin/admin_main_homepage.html', context=diction)
