# forms.py
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class House_Area_Form(forms.Form):
    Area = forms.IntegerField(label='')
    # Area = forms.IntegerField(label='',
    #         validators=[
    #         MinValueValidator(2100, message='Value must be greater than or equal to 2100'),
    #         MaxValueValidator(5100, message='Value must be less than or equal to 5100')
    #     ])
