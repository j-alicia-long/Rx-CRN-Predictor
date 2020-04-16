from django import forms
from .models import Patient

class PatientIntakeForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
