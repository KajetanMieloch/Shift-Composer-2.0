from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Employee, Availability, Position
from organisation.models import Organisation
from .forms import AddPositionForm, AddEmployeeForm, AvailabilityForm
from django.contrib import messages
from datetime import datetime


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
    
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            employee = Employee.objects.get(pk=employee_id)
            days = request.POST['days']
            availability = request.POST['availability']
            availability_hours_start = request.POST['availability_hours_start']
            availability_hours_end = request.POST['availability_hours_end']
                      
            try:
                request.POST['may_be_extended']
                may_be_extended = True
            except:
                may_be_extended = False
            
            for date in days.split(','):
                cleaned_date = (date.replace('[', '').replace(']', '').strip())[:-1][1:]
                parts = cleaned_date.split('-')
                year, month, day = parts[0], parts[1], parts[2]
                day = day.zfill(2)
                month = month.zfill(2)
                formatted_date = f'{year}-{month}-{day}'
                
                if availability_hours_start == '':
                    availability_hours_start = None
                if availability_hours_end == '':
                    availability_hours_end = None
                
                print(formatted_date)
                availability_obj = Availability(employee=employee, day=formatted_date, availability=availability, availability_hours_start=availability_hours_start, availability_hours_end=availability_hours_end, may_be_extended=may_be_extended)
                availability_obj.save()
                print(availability)
            
            messages.success(request, f'Availability added successfully')
        else:
            messages.error(request, f'Availability not added')

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
            return render(request, 'employees/details.html',{
                'user': request.user,
                'employee': employee,
                'availabilities': employeeAvailabilities,
                'form': AvailabilityForm(),
            })
    except:
        messages.error(request, f'Employee not found')
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



#TODO Add search functionality (search by name, surname, position)
#TODO Add multiple availabilities at once
#TODO Delete multiple availabilities and or employees at once