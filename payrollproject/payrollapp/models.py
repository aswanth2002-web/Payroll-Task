from django.db import models

# Create your models here.

class employeedetails(models.Model):
    emp_name=models.CharField(max_length=50)
    emp_id=models.CharField(max_length=10)
    designation=models.CharField(max_length=50)
    joining_date=models.DateField()
    basic_salary=models.FloatField()
    hra=models.FloatField()
    da=models.FloatField()
    allowance=models.FloatField()
    pf=models.FloatField()
    esi=models.FloatField()
    
    def __str__(self):
        return self.emp_name

class leavedetails(models.Model):
    emp=models.ForeignKey(employeedetails,on_delete=models.CASCADE)
    month=models.CharField(max_length=20)
    leave_days=models.IntegerField()
    def __str__(self):
        return self.emp.emp_name
    

