from django.urls import path
from . import admin_views, manager_views, employee_views, views

app_name = 'medicine'

urlpatterns = [
    path('', views.main_home_page, name='main_home'),
    # admin urls
    path('admin/add_company/', admin_views.AddCompany.as_view(), name='add_company'),
    path('admin/view_company', admin_views.company_view, name='company_view'),
    path('admin/add_medicine/', admin_views.CreateMedicine.as_view(), name='admin_add_medicine'),
    path('admin/medicine_view', admin_views.medicine_view, name='admin_medicine_view'),
    path('admin/update/<pk>/', admin_views.UpdateMedicine.as_view(), name='admin_update_medicine'),
    path('admin/delete_medicine/<pk>/', admin_views.MedicineDelete.as_view(), name='admin_delete_medicine'),
    path('admin/search/', admin_views.search_medicine, name='admin_search_medicine'),
    path('admin/expire_date/', admin_views.search_medicine_expire_date, name='admin_view_expire_date'),
    path('admin/receipt', admin_views.receipt, name='admin_receipt'),
    path('admin/all_sales', admin_views.all_sales, name='admin_all_sales'),
    path('admin/receipt_detail/<int:receipt_id>/', admin_views.receipt_detail, name='admin_receipt_details'),
    path('admin/issue_item/<pk>/', admin_views.issue_item, name='admin_issue_item'),
    path('admin/add_to_stock/<pk>/', admin_views.add_to_stock, name='admin_add_to_stock'),
    path('admin/sell/product', admin_views.sell_product_detail, name='admin_sell_product'),
    path('update_company/<pk>/', admin_views.UpdateCompany.as_view(), name='admin_update_company'),
    path('delete_company/<pk>/', admin_views.CompanyDelete.as_view(), name='admin_delete_company'),
    path('search_company/', admin_views.search_company, name='admin_search_company'),

    # manager urls
    path('manger/add_company/', manager_views.AddCompany.as_view(), name='manager_add_company'),
    path('manager/view_company/', manager_views.company_view, name='manager_company_view'),
    path('manager/update_company/<pk>/', manager_views.UpdateCompany.as_view(), name='manager_update_company'),
    path('manager/delete_company/<pk>/', manager_views.CompanyDelete.as_view(), name='manager_delete_company'),
    path('manager/search_company/', manager_views.search_company, name='manager_search_company'),
    path('manager/medicine_view', manager_views.medicine_view, name='manager_medicine_view'),
    path('manager/add_medicine/', manager_views.CreateMedicine.as_view(), name='manager_add_medicine'),
    path('manager/update/<pk>/', manager_views.UpdateMedicine.as_view(), name='manager_update_medicine'),
    path('manager/delete_medicine/<pk>/', manager_views.MedicineDelete.as_view(), name='manager_delete_medicine'),
    path('manager/search/', manager_views.search_medicine, name='manager_search_medicine'),
    path('manager/expire_date/', manager_views.search_medicine_expire_date, name='manager_view_expire_date'),
    path('manager/receipt', manager_views.receipt, name='manager_receipt'),
    path('manager/all_sales', manager_views.all_sales, name='manager_all_sales'),
    path('manager/receipt_detail/<int:receipt_id>/', manager_views.receipt_detail, name='manager_receipt_details'),
    path('manager/issue_item/<pk>/', manager_views.issue_item, name='manager_issue_item'),
    path('manager/add_to_stock/<pk>/', manager_views.add_to_stock, name='manager_add_to_stock'),
    path('manager/sell/product', manager_views.sell_product_detail, name='manager_sell_product'),


    # employee urls
    path('employee/add_company/', employee_views.AddCompany.as_view(), name='employee_add_company'),
    path('employee/view_company/', employee_views.company_view, name='employee_company_view'),
    path('employee/update_company/<pk>/', employee_views.UpdateCompany.as_view(), name='employee_update_company'),
    path('employee/delete_company/<pk>/', employee_views.CompanyDelete.as_view(), name='employee_delete_company'),
    path('employee/search_company/', employee_views.search_company, name='employee_search_company'),
    path('employee/medicine_view', employee_views.medicine_view, name='employee_medicine_view'),
    path('employee/add_medicine/', employee_views.CreateMedicine.as_view(), name='employee_add_medicine'),
    path('employee/update/<pk>/', employee_views.UpdateMedicine.as_view(), name='employee_update_medicine'),
    path('employee/delete_medicine/<pk>/', employee_views.MedicineDelete.as_view(), name='employee_delete_medicine'),
    path('employee/search/', employee_views.search_medicine, name='employee_search_medicine'),
    path('employee/expire_date/', employee_views.search_medicine_expire_date, name='employee_view_expire_date'),
    path('employee/receipt', employee_views.receipt, name='employee_receipt'),
    path('employee/all_sales', employee_views.all_sales, name='employee_all_sales'),
    path('employee/receipt_detail/<int:receipt_id>/', employee_views.receipt_detail, name='employee_receipt_details'),
    path('employee/issue_item/<pk>/', employee_views.issue_item, name='employee_issue_item'),
    path('employee/add_to_stock/<pk>/', employee_views.add_to_stock, name='employee_add_to_stock'),
    path('employee/sell/product', employee_views.sell_product_detail, name='employee_sell_product'),

]