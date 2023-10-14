from django.shortcuts import render
from core.models import UserProfile
from .models import Organisation
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


@login_required
def index(request):

    return render(request, 'organisation/index.html', {
        'user': request.user,
        'in_organisation': UserProfile.objects.get(user=request.user).in_organisation,
        'is_admin': UserProfile.objects.get(user=request.user).is_admin,
        'organisation': Organisation.objects.get(members__user=request.user),
        })

def create(request):
    return render(request, 'organisation/create.html', {
        'user': request.user,
        'in_organisation': UserProfile.objects.get(user=request.user).in_organisation,
        'is_admin': UserProfile.objects.get(user=request.user).is_admin,
        'organisation': Organisation.objects.get(members__user=request.user),
        })

def join(request):
    return render(request, 'organisation/join.html')

def leave(request):
    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.in_organisation = False
    user_profile.is_admin = False
    user_profile.save()

    return redirect('organisation:index')

def delete(request):
    return render(request, 'organisation/delete.html')