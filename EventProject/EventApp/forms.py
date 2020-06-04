from django import forms
from EventApp.models import *

class ChildDetailForm(forms.ModelForm):
    class Meta:
        model=ChildDetail
        fields='__all__'



class VolDetailForm(forms.ModelForm):
    class Meta:
        model=VolDetail
        Reason = forms.CharField(label='Why u want to join Us..')
        fields='__all__'


class DonDetailForm(forms.ModelForm):
    class Meta:
        model=DonDetail
        fields='__all__'
