from django.shortcuts import render
from .forms import SelectEmployeeForm
from django.shortcuts import redirect
from organisation.models import Organisation
from employees.models import Employee


def index(request):

    try:
        org = Organisation.objects.get(members__user=request.user)
    except:
        return redirect('organisation:notinorg')
    
    if request.method == 'POST':
        selected_employees = request.POST.getlist('selected_employees')
        mode = request.POST.get('mode')
        employeeList = []
        if mode == 'ava':            
            for i in range(len(selected_employees)):
                employee = Employee.objects.get(id=selected_employees[i])
                employeeList.append(employee)
        
            
                
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            print('----------------')
            print(selected_employees)
        else:
            print("Comming soon!")

    return render(request, 'generator/index.html',{
        'form': SelectEmployeeForm(org),
    })