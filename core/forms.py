from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class LoginForm(AuthenticationForm):
    
    class Meta:
        fields = ['username', 'password', 'captcha']
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none',
        'placeholder': 'Kajetan',
        }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none',
        'placeholder': '******',
        }))
    
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none',
        'placeholder': 'Kajetan',
        }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none',
        'placeholder': 'example@example.com',
        }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none',
        'placeholder': '******',
        }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none',
        'placeholder': '******',
        }))