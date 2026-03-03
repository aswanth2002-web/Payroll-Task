from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.conf import settings

# Create your views here.

def emp_registration(request):
    if(request.method=='POST'):
        emp_name=request.POST.get('emp_name')
        emp_id=request.POST.get('emp_id')
        designation=request.POST.get('designation')
        joining_date=request.POST.get('joining_date')
        basic_salary=request.POST.get('basic_salary')
        hra=request.POST.get('hra')
        da=request.POST.get('da')
        allowance=request.POST.get('allowance')
        pf=request.POST.get('pf')
        esi=request.POST.get('esi')
        data=employeedetails(emp_name=emp_name,emp_id=emp_id,designation=designation,joining_date=joining_date,basic_salary=basic_salary,hra=hra,da=da,pf=pf,allowance=allowance,esi=esi)
        data.save()
        return redirect(emp_loginpage)   
    return render(request,'registration.html')

def emp_loginpage(request):
    if (request.method=='POST'):
        emp_name=request.POST.get('emp_name')
        emp_id=request.POST.get('emp_id')
        data=employeedetails.objects.all()
        for i in data:
            if(i.emp_name==emp_name and i.emp_id==emp_id):
                request.session['userid']=i.id
                return redirect(empleave)
        else:
            return HttpResponse('failed')
    return render(request,'emp_login.html')          


def empleave(request):
    id1= request.session.get('userid')
    emp=employeedetails.objects.get(id=id1)
    if (request.method=='POST'):
        month=request.POST.get('month')
        leave_days=request.POST.get('leave_days')
        data=leavedetails(emp=emp,month=month,leave_days=leave_days)
        data.save()
        return redirect(payslip)
    return render(request,'empleave.html')

def payslip(request):
    userid=request.session['userid']
    data=employeedetails.objects.get(id=userid)
    db=leavedetails.objects.filter(emp=data).last()
    month=db.month
    
    if db:
        leave_days= db.leave_days
    else:
        leave_days=0    

    basic_salary=data.basic_salary
    hra=basic_salary*data.hra/100 
    da=basic_salary*data.da/100
    allowance=basic_salary*data.allowance/100
    pf=basic_salary*data.pf/100
    leave_deduction=(basic_salary/30)*leave_days

    working_days=30-leave_days

    gross_salary=(basic_salary + hra + da + allowance)

    
    if gross_salary <=21000 and gross_salary>=0 :
        esi=gross_salary*data.esi/100
    else:
        esi=0
    deduction=pf + esi

    total_salary=gross_salary - leave_deduction - deduction

    return render(request,'payslip.html',{'data':data,'total_salary':total_salary,'leave_days':leave_days,'month':month,'gross_salary':gross_salary,'leave_deduction':leave_deduction,'working_days':working_days})

def emp_list(request):
    emp_db=employeedetails.objects.all()
    data=leavedetails.objects.all()
    return render(request,'emp_list.html',{'emp_db':emp_db,'data':data}) 
   






        


