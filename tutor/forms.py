from django import forms
from .models import *


class ProfileCreateForm(forms.ModelForm):

    class Meta:
        model = TutorProfile
        fields = ['bio', 'method', 'fee', 'zipcode', 'subjects', 'resume', 'contact_info']
        widgets = {
            'subjects': forms.CheckboxSelectMultiple()
        }


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = TutorProfile
        fields = ['bio', 'method', 'fee', 'zipcode', 'subjects', 'resume', 'contact_info']
        widgets = {
            'subjects': forms.CheckboxSelectMultiple()
        }
