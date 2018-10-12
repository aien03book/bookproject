from django import forms
from django.contrib.auth.models import User
from .models import Order



class Add_form(forms.ModelForm):
    time = forms.DateField()
    class Meta:
        model = Order
        fields = [
            'time',
        ]