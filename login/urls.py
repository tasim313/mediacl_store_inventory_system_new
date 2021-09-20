from django.urls import path
from . import views, admin_views, manager_views, employee_views

app_name = 'App_Login'

urlpatterns = [
    path('signup/admin/', views.AdminSignUpView.as_view(), name='admin_signup'),
    path('signup/manager/', views.ManagerSignUpView.as_view(), name='manager_signup'),
    path('signup/employee/', views.EmployeeSignUpView.as_view(), name='employee_signup'),
    path('user_login/', views.user_login, name='user_login'),
    path('login/', views.login_page, name='login'),
    path('profile/admin/', admin_views.Profile.as_view(), name='admin_profile'),
    path('index/admin/', admin_views.index, name='index'),
    path('profile/manager/', manager_views.Profile.as_view(), name='manager_profile'),
    path('index/manager/', manager_views.index, name='manager_index'),
    path('profile/employee/', employee_views.EmployeeProfile.as_view(), name='employee_profile'),
    path('index/employee/', employee_views.index, name='employee_index'),
    path('employee_details/', admin_views.employee_view, name='employee'),
    path('manager_details/', admin_views.manager_view, name='manager'),
    path('logout/', views.logout_user, name='logout'),
    #admin dashboard
    path('home/', admin_views.admin_dashboard, name='admin_main_home'),
    #manager dashboard
    path('manager/home/', manager_views.manager_dashboard, name='manager_main_home'),
    #employee dashboard
    path('employee/home/', employee_views.employee_dashboard, name='employee_main_home'),
]

