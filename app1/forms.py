from django import forms
from django.forms import CheckboxSelectMultiple, ModelForm, MultipleChoiceField

from .models import *




class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'


class UserForm(ModelForm):
    class Meta:
        model = Utilisateur
        fields = '__all__'
        exclude=['user']




class AvailabilityForm(forms.Form):
    check_in = forms.DateTimeField(required=True,
                                   input_formats=['%d/%m/%YT%H:%M', ],
                                   widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    check_out = forms.DateTimeField(required=True,
                                    input_formats=['%d/%m/%YT%H:%M', ],
                                    widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    

class AvaForm(ModelForm):
    check_in = forms.DateTimeField(required=True,
                                   input_formats=['%d/%m/%YT%H:%M', ],
                                   widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    check_out = forms.DateTimeField(required=True,
                                    input_formats=['%d/%m/%YT%H:%M', ],
                                    widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    class Meta:
        model = Reservation
        fields = ('check_in','check_out')