from django.shortcuts import render
from .forms import SelectEmployeeForm
from django.shortcuts import redirect
from organisation.models import Organisation


def index(request):

    try:
        org = Organisation.objects.get(members__user=request.user)
    except:
        return redirect('organisation:notinorg')
    
    if request.method == 'POST':
        print(request.POST['selected_employees'])    

    return render(request, 'generator/index.html',{
        'form': SelectEmployeeForm(org),
    })