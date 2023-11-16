from django.forms import ModelForm
from django import forms
from .models import *

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'

class DroneForm(forms.ModelForm):
    class Meta:
        model = Drone
        fields = '__all__'

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = '__all__'

class DronePermitForm(forms.ModelForm):
    class Meta:
        model = DronePermit
        fields = ['purpose',]