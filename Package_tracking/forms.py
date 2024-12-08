# from django import forms
# forms.py
from django import forms
from .models import Package

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['sender_name', 'receiver_name', 'receiver_email', 'status']


class TrackingForm(forms.Form):
    tracking_id = forms.UUIDField(
         
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your tracking code. e.g. 987733733-GT'}),
    )
