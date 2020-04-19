from django import forms
from .models import Patient

class PatientIntakeForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ('crn_score',)

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'other_info': forms.Textarea(attrs={'class': 'form-control'}),
            }
