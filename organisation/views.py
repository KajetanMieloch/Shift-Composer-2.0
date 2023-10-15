from django.shortcuts import render
from core.models import UserProfile
from .models import Organisation
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from organisation.forms import CreateOrganisation
import random
import string
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from .models import Invitation


@login_required
def index(request):
    
    try:
        Organisation.objects.get(members__user=request.user)
    except:
        return redirect('organisation:notinorg')

    return render(request, 'organisation/index.html', {
        'user': request.user,
        'in_organisation': Organisation.objects.get(members__user=request.user).members.filter(user=request.user).exists(),
        'is_admin': Organisation.objects.get(members__user=request.user).admins.filter(user=request.user).exists(),
        'organisation': Organisation.objects.get(members__user=request.user),
        })

@login_required
def notinorg(request):
    
    try:
        Organisation.objects.get(members__user=request.user)
        return redirect('organisation:index')
    except:
        pass
    
    return render(request, 'organisation/notinorg.html', {
        'user': request.user,
        })

@login_required
def join(request):
    return render(request, 'organisation/join.html')

@login_required
def leave(request):
    user_profile = UserProfile.objects.get(user=request.user)
    try:
        organisation = Organisation.objects.get(members__user=request.user)
        organisation.members.remove(user_profile)
        organisation.admins.remove(user_profile)
        organisation.save()
    except:
        pass

    return redirect('organisation:index')

@login_required
def delete(request):
    try:
        organisation = Organisation.objects.get(members__user=request.user)
        organisation.delete()
    except:
        pass

    return redirect('organisation:index')

@login_required
def create(request):
    try:
        Organisation.objects.get(members__user=request.user)
        return redirect('organisation:index')
    except:
        pass

    if request.method == 'POST':
        form = CreateOrganisation(request.POST)
        if form.is_valid():
            organisation = Organisation(name=form.cleaned_data['name'])
            organisation.save()
            organisation.members.add(UserProfile.objects.get(user=request.user))
            organisation.admins.add(UserProfile.objects.get(user=request.user))
            organisation.save()
            return redirect('organisation:index')
    
    return render(request, 'organisation/create.html', {
        'field': CreateOrganisation(),
        })

@login_required
def remove(request, user_id):
    print(user_id)
    try:
        organisation = Organisation.objects.get(members__user=request.user)
        if organisation.admins.filter(user=request.user).exists():
            user_profile = UserProfile.objects.get(id=user_id)
            organisation.members.remove(user_profile)
            organisation.admins.remove(user_profile)
            organisation.save()
    except:
        pass
    
    return redirect('organisation:index')


def generate_code():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

@login_required
def generate(request):
    try:
        organisation = Organisation.objects.get(members__user=request.user)
        if organisation.admins.filter(user=request.user).exists():
            code = generate_code()
            invitation = Invitation(code=code, organisation=organisation, expires=datetime.now() + timedelta(days=1))
            print(invitation)
            invitation.save()
            return render(request, 'organisation/index.html', {
                'user': request.user,
                'in_organisation': Organisation.objects.get(members__user=request.user).members.filter(user=request.user).exists(),
                'is_admin': Organisation.objects.get(members__user=request.user).admins.filter(user=request.user).exists(),
                'organisation': Organisation.objects.get(members__user=request.user),
                'code': code,
                })
    except:
        pass
    
    return redirect('organisation:index')