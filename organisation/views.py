from django.shortcuts import render
from core.models import UserProfile
from .models import Organisation
from django.contrib.auth.decorators import login_required


@login_required
def index(request):

    return render(request, 'organisation/index.html', {
        'user': request.user,
        'in_organisation': UserProfile.objects.get(user=request.user).in_organisation,
        'organisation': Organisation.objects.get(members__user=request.user),
        })

def create(request):
    return render(request, 'organisation/create.html')

def join(request):
    return render(request, 'organisation/join.html')