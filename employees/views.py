from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Employee, Availability, Position
from organisation.models import Organisation
from .forms import AddPositionForm, AddEmployeeForm
from django.contrib import messages

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
        'addEmployeeForm': AddEmployeeForm(org=userOrganisation),
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
            messages.success(request, f'{employee} deleted successfully')
        else:
            messages.error(request, f'Employee not found')
    except:
        messages.error(request, f'Employee not found')
        pass

    return redirect('employees:index')

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

    return redirect('employees:index')

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
        alreadyExistingPositions = Position.objects.filter(organisation=userOrganisation, position=position)
        if not alreadyExistingPositions:
            position.save()
            messages.success(request, f'Position {position} added successfully')
        else:
            messages.error(request,f'Position {position} already exists')
            pass

    return redirect('employees:index')

@login_required
def add_employee(request):

    try:
        Organisation.objects.get(members__user=request.user)
    except:
        return redirect('organisation:notinorg')

    userOrganisation = Organisation.objects.get(members__user=request.user)
    allEmployeesInOrganisation = Employee.objects.filter(organisation=userOrganisation)

    if request.method == 'POST':
        print(request.POST)
        name = request.POST['name']
        surname = request.POST['surname']
        position = Position.objects.get(pk=request.POST['position'])
        employee = Employee(organisation=userOrganisation, name=name, surname=surname, position=position)
        employee.save()
        messages.success(request, f'{employee} added successfully')

    return redirect('employees:index')