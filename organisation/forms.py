from django import forms

class CreateOrganisation(forms.Form):
    
    class Meta:
        fields = ['name']
    
    name = forms.CharField(max_length=100)