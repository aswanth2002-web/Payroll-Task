from django.urls import path
from .views import *

urlpatterns = [
    path('register/',emp_registration),
    path('login/',emp_loginpage),
    path('list/',emp_list),
    path('leave/',empleave),
    path('payslip/',payslip)
    # path('empview/',emp_view)

]
