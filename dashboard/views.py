from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from organisation.models import Organisation


@login_required
def index(request):
    try:
        Organisation.objects.get(members__user=request.user)
    except:
        return redirect('organisation:notinorg')
    
    return render(request, 'dashboard/index.html')
