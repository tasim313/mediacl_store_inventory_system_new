from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import MedicineProduct, Company
from django.urls import reverse, reverse_lazy


def company_view(request):
    company_list = Company.objects.all()
    diction = {'company_list': company_list}
    return render(request, "company/company_list.html", context=diction)


class CreateCompany(CreateView):
    model = Company
    template_name = 'company/create_company.html'
    fields = ('name', 'lic_no', 'address', 'cont_num', 'email', 'description')

    def form_valid(self, form):
        company_create = form.save(commit=False)
        company_create.save()
        return HttpResponseRedirect(reverse('medicine:company_list'))


class UpdateCompany(UpdateView):
    model = Company
    fields = ('name', 'lic_no', 'address', 'cont_num', 'email', 'description')
    template_name = 'company/update_company.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('medicine:company_list', kwargs={})


class CompanyDelete(DeleteView):
    context_object_name = 'company'
    model = Company
    success_url = reverse_lazy('medicine:company_list')
    template_name = 'company/Delete_company.html'


def search_company(request):
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = Company.objects.filter(name__icontains=search)
    return render(request, 'company/search_company.html', context={'search': search, 'result': result})



