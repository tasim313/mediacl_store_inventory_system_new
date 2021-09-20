from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.views.generic import CreateView

from .models import CustomUser, Admin, Manager
from .forms import AdminSignUpForm, ManagerSignUpForm, EmployeeSignUpForm
from django.shortcuts import render, HttpResponse, HttpResponseRedirect


class ManagerSignUpView(CreateView):
    model = CustomUser
    form_class = ManagerSignUpForm
    template_name = 'new_registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'manager'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('App_Login:login')


class AdminSignUpView(CreateView):
    model = CustomUser
    form_class = AdminSignUpForm
    template_name = 'new_registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Pharmacy Shop Owner or Pharmacy Super Admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('App_Login:login')


class EmployeeSignUpView(CreateView):
    model = CustomUser
    form_class = EmployeeSignUpForm
    template_name = 'new_registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Pharmacy Employee'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('App_Login:login')


def login_page(request):
    return render(request, 'App_Login/login.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'new.html')
            else:
                return HttpResponse('Account is not active !!')
        else:
            return HttpResponse('Account Details are wrong !....')
    else:
        return HttpResponse('Account Details are wrong  2 !....')


def logout_user(request):
    logout(request)
    return redirect('App_Login:login')

