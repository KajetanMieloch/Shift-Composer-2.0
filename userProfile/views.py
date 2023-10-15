from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import UserProfile
from organisation.models import Organisation

@login_required
def index(request):
    return render(request, 'userProfile/index.html',{
        'user': request.user,
        'user_profile': UserProfile.objects.get(user=request.user),
        'in_organisation': Organisation.objects.get(members__user=request.user).members.filter(user=request.user).exists(),
        'is_admin': Organisation.objects.get(members__user=request.user).admins.filter(user=request.user).exists(),
        'organisation': Organisation.objects.get(members__user=request.user),
    })