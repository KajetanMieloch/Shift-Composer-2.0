from django.shortcuts import render
from django.shortcuts import redirect
from .forms import SignupForm
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode

from .forms import LoginForm

from .tokens import account_activation_token

def index(request):
    return render(request, 'core/index.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            if not user.is_active:
                messages.error(request, 'Your account is not activated. Please check your email for an activation link.')
            else:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('dashboard:index')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except:
        user = None
        
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        
        messages.success(request, f'Dear {user.username}, your account has been activated. You can now log in.')
        return redirect('core:login')
    else:
        messages.error(request, 'An error occurred while activating your account.')
    return redirect('core:login')

def activateEmail(request, user, to_email):
    mail_subject = 'Activate your ShiftComposer account.'
    message = render_to_string("template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear {user.username}, we have sent you an email to {to_email} with an activation link. Please click on it to activate your account.')
    else:
        messages.error(request, f'An error occurred while sending an email to {to_email}.')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # Create a UserProfile object for the new user
            UserProfile.objects.create(user=user)

            activateEmail(request, user, form.cleaned_data.get('email'))
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form': form})