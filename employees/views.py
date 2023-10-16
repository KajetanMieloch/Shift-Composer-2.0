from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Employee, Availability, Position
from organisation.models import Organisation
from .forms import AddPositionForm, AddEmployeeForm

@login_required
def index(request):

    try:
        Organisation.objects.get(members__user=request.user)
    except:
        return redirect('organisation:notinorg')

    userOrganisation = Organisation.objects.get(members__user=request.user)
    allEmployeesInOrganisation = Employee.objects.filter(organisation=userOrganisation)

    return render(request, 'employees/index.html',{
        'user': request.user,
        'employees': allEmployeesInOrganisation,
        'addPositionForm': AddPositionForm(),
        'addEmployeeForm': AddEmployeeForm(),
    })

@login_required
def delete(request, employee_id):

    try:
        Organisation.objects.get(members__user=request.user)
    except:
        return redirect('organisation:notinorg')

    userOrganisation = Organisation.objects.get(members__user=request.user)
    allEmployeesInOrganisation = Employee.objects.filter(organisation=userOrganisation)

    try:
        employeeOrganisation = Employee.objects.get(pk=employee_id).organisation
        if userOrganisation == employeeOrganisation:
            employee = Employee.objects.get(pk=employee_id)
            employee.delete()
    except:
        pass

    return render(request, 'employees/index.html',{
        'user': request.user,
        'employees': allEmployeesInOrganisation,
        'addPositionForm': AddPositionForm(),
        'addEmployeeForm': AddEmployeeForm(),
    })

@login_required
def details(request, employee_id):

    try:
        Organisation.objects.get(members__user=request.user)
    except:
        return redirect('organisation:notinorg')
    
    userOrganisation = Organisation.objects.get(members__user=request.user)

    try:
        employeeOrganisation = Employee.objects.get(pk=employee_id).organisation
        if userOrganisation == employeeOrganisation:
            employee = Employee.objects.get(pk=employee_id)
            employeeAvailabilities = Availability.objects.filter(employee=employee)
    except:
        pass

    return render(request, 'employees/details.html',{
        'user': request.user,
        'employee': employee,
        'employeeAvailabilities': employeeAvailabilities,
        'addPositionForm': AddPositionForm(),
        'addEmployeeForm': AddEmployeeForm(),
    })

@login_required
def add_position(request):

    try:
        Organisation.objects.get(members__user=request.user)
    except:
        return redirect('organisation:notinorg')

    userOrganisation = Organisation.objects.get(members__user=request.user)
    allEmployeesInOrganisation = Employee.objects.filter(organisation=userOrganisation)

    print(request.method)

    if request.method == 'POST':
        position = request.POST['position']
        position = Position(organisation=userOrganisation, position=position)
        if position not in Position.objects.filter(organisation=userOrganisation):
            position.save()
        else:
            #Here will be message that position already exists
            pass

    return render(request, 'employees/index.html',{
        'user': request.user,
        'employees': allEmployeesInOrganisation,
        'addPositionForm': AddPositionForm(),
        'addEmployeeForm': AddEmployeeForm(),
    })

@login_required
def add_employee(request):

    try:
        Organisation.objects.get(members__user=request.user)
    except:
        return redirect('organisation:notinorg')

    userOrganisation = Organisation.objects.get(members__user=request.user)
    allEmployeesInOrganisation = Employee.objects.filter(organisation=userOrganisation)

    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        position = request.POST['position']
        employee = Employee(organisation=userOrganisation, name=name, surname=surname, position=position)
        employee.save()

    return render(request, 'employees/index.html',{
        'user': request.user,
        'employees': allEmployeesInOrganisation,
        'addPositionForm': AddPositionForm(),
        'addEmployeeForm': AddEmployeeForm(),
    })