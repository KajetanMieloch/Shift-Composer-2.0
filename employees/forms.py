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
    position = forms.ModelChoiceField(queryset=Position.objects.none())

    def __init__(self, org, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['position'].queryset = Position.objects.filter(organisation=org.id)
        from django import forms

class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['availability']

