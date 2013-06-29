# -*- coding: utf-8 -*-
"""
All the forms located here.
"""

from django import forms
from django.core.exceptions import ValidationError


##### validators ########
def valid_fixed_length(value):
    if len(value) == 18 or len(value) == 15:
        return True
    else:
        raise ValidationError(u'should length in 15 or 18')


#### forms #######
class SignUpForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    real_name = forms.CharField()
    real_id = forms.CharField(validators=[valid_fixed_length])
    location_province = forms.CharField()
    location_city = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()


class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
