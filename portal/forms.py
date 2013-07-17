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


class ChargeRentForm(forms.Form):
    house_type = forms.ChoiceField(choices=[
        ('1', '1 room'),
        ('2', '2 room'),
        ('3', '3 room'),
        ('4', '>=4 room')
    ])

    house_decoration = forms.ChoiceField(choices=[
        ('1', 'no'),
        ('2', 'basic'),
        ('3', 'medium'),
        ('4', 'high'),
    ])

    house_size = forms.CharField()

    location_province = forms.CharField()
    location_city = forms.CharField()
    location_zone = forms.CharField()
    location_area = forms.CharField()
    location_building = forms.CharField()

    owner_name = forms.CharField()
    owner_real_id = forms.CharField()

    bank_name = forms.CharField()
    bank_card_id = forms.CharField()
    bank_location_province = forms.CharField()
    bank_location_city = forms.CharField()
	

class PasswordModifyForm(forms.Form):
    password = forms.CharField()
    new_password = forms.CharField()
    confirm_new_password = forms.CharField()
	

class PhoneModifyForm(forms.Form):
    phone = forms.CharField()
    verification_code = forms.CharField()
	

class MailboxBindingForm(forms.Form):
    email = forms.EmailField()
    
class NameCertificationForm(forms.Form):
    real_name = forms.CharField()
    real_id = forms.CharField(validators=[valid_fixed_length])
    
class SecurityProblemForm(forms.Form):
    problem_one = forms.CharField()
    problem_two = forms.CharField()
    problem_three = forms.CharField()