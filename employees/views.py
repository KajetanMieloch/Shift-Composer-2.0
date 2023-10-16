from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Employee, Availability
from organisation.models import Organisation

@login_required
def index(request):

    userOrganisation = Organisation.objects.get(members__user=request.user)
    allEmployeesInOrganisation = Employee.objects.filter(organisation=userOrganisation)

    return render(request, 'employees/index.html',{
        'user': request.user,
        'employees': allEmployeesInOrganisation,
    })

@login_required
def delete(request, employee_id):

    userOrganisation = Organisation.objects.get(members__user=request.user)
    employeeOrganisation = Employee.objects.get(pk=employee_id).organisation

    allEmployeesInOrganisation = Employee.objects.filter(organisation=userOrganisation)

    try:
        if userOrganisation == employeeOrganisation:
            employee = Employee.objects.get(pk=employee_id)
            employee.delete()
    except:
        pass

    return render(request, 'employees/index.html',{
        'user': request.user,
        'employees': allEmployeesInOrganisation,
    })

@login_required
def details(request, employee_id):
    
    if request.user == Employee.objects.get(pk=employee_id).organisation.user:
        employee = Employee.objects.get(pk=employee_id)
        availability = Availability.objects.filter(employee=employee)
    
    return render(request, 'employees/details.html',{
        'user': request.user,
        'employee': employee,
        'availability': availability,
    })