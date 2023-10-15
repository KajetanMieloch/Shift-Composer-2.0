from django import forms

class userprofile(forms.Form):
    
    class Meta:
        fields = ['username', 'name', 'surename', 'photo']
    
    username = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    surename = forms.CharField(max_length=100)
    photo = forms.ImageField(upload_to='profile_pics', blank=True)