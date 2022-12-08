from django import forms 

class NameForm(forms.Form):
    location = forms.CharField(label = "Location", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Location'}))
