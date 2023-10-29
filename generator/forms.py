from django import forms
from employees.models import Employee, Position, Availability
from core.models import UserProfile

class SelectEmployeeForm(forms.Form):
    class Meta:
        fields = ['employee']
    employee = forms.ModelChoiceField(queryset=Employee.objects.none())

    def __init__(self, org, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employee'].queryset = Employee.objects.filter(organisation=org.id)
    
