from django import forms
from employees.models import Employee, Position, Availability
from core.models import UserProfile

class SelectEmployeeForm(forms.Form):
    available_employees = forms.ModelMultipleChoiceField(queryset=Employee.objects.none())
    selected_employees = forms.ModelMultipleChoiceField(queryset=Employee.objects.none())

    def __init__(self, org, *args, **kwargs):
        super().__init__(*args, **kwargs)
        emptyQueryset = Employee.objects.none()
        queryset = Employee.objects.filter(organisation=org)
        self.fields['available_employees'].queryset = queryset
        self.fields['selected_employees'].queryset = emptyQueryset
        
        self.fields['available_employees'].widget.attrs['class'] = 'form-control'
        self.fields['selected_employees'].widget.attrs['class'] = 'form-control'