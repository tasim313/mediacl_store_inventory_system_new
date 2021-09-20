from django import forms
from django.contrib.auth.forms import UserCreationForm


from .models import Admin, Manager, Employee, CustomUser


class AdminSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = True
        if commit:
            user.save()
        return user


class ManagerSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_manager = True
        user.save()
        if commit:
            user.save()
        return user


class EmployeeSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_employee = True
        user.save()
        if commit:
            user.save()
        return user

