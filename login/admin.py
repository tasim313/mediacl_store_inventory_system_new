from django.contrib import admin

# Register your models here.

from .models import CustomUser, Admin, Manager, Employee


admin.site.register(CustomUser)
admin.site.register(Admin)
admin.site.register(Manager)
admin.site.register(Employee)