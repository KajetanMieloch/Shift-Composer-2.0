from django.shortcuts import render
from django.shortcuts import redirect
from .forms import SignupForm

def index(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            
                
            return redirect('/login')
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html', {
        'form': form,
    })
