from django.shortcuts import render
from .forms import SelectEmployeeForm
from django.shortcuts import redirect
from organisation.models import Organisation
from employees.models import Employee, Availability
from .employeeClass import Employee as Employee_class


def index(request):

    try:
        org = Organisation.objects.get(members__user=request.user)
    except:
        return redirect('organisation:notinorg')
    
    if request.method == 'POST':
                
        employeeList = []
                
        
        selected_employees = request.POST.getlist('selected_employees')
        mode = request.POST.get('mode')

        if mode == 'ava':            
            for i in range(len(selected_employees)):
                employee = Employee.objects.get(id=selected_employees[i])
                availability = Availability.objects.filter(employee=employee)
                
                
                employee_availabilities = []
                for a in availability:
                    employee_availabilities.append({'day': a.day, 'availability': a.availability})
                
                employee_availability_hours = []
                for h in availability:
                    employee_availability_hours.append({'day': h.day, 'start': h.availability_hours_start, 'end': h.availability_hours_end})
               
                employeeList.append(Employee_class(employee.id, employee.name, employee.surname, employee.position.position, employee_availabilities, employee_availability_hours))
                
                print(employeeList)                        

        else:
            print("Comming soon!")

    return render(request, 'generator/index.html',{
        'form': SelectEmployeeForm(org),
    })