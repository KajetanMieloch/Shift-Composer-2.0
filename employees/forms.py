from django import forms
from .models import Employee, Position, Availability

class AddPositionForm(forms.Form):

    class Meta:
        fields = ['position']

    position = forms.CharField(label='Position', max_length=100)

class AddEmployeeForm(forms.Form):

    class Meta:
        fields = ['name', 'surname', 'position']

    name = forms.CharField(label='Name', max_length=100)
    surname = forms.CharField(label='Surname', max_length=100)
    position = forms.ModelChoiceField(queryset=Position.objects.all())