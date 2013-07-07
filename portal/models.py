# -*- coding: utf-8 -*-
"""
Database models are defined here.
"""
from django.forms.models import model_to_dict
from django.db.models import Model
from django.db.models import IntegerField, CharField, DateTimeField
from django.db.models import DateField, EmailField, BooleanField
from django.db.models import ForeignKey, OneToOneField
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


class BaseModel(object):
    def as_dict(self):
        return model_to_dict(self)

    def update_from_dict(self, new_fields):
        for key, value in new_fields.items():
            setattr(self, key, value)


class User(Model, BaseModel):
    username = CharField(max_length=255, db_index=True, unique=True)
    password = CharField(max_length=255)
    phone = CharField(max_length=20, db_index=True)
    real_name = CharField(max_length=255)
    real_id = CharField(max_length=40)
    email = EmailField()
    signup_at = DateTimeField(auto_now=True)
    avater = CharField(max_length=255)
    location_province = CharField(max_length=255)
    location_city = CharField(max_length=255)


class UserAdmin(admin.ModelAdmin):
    list_display = ['username']


##################################
class LandlordRentProfile(Model, BaseModel):
    """A user who is landlord can have many rent."""
    landlord = ForeignKey(User)

    rent_type = CharField(_('rent_type'), max_length=2,
                                 choices=[('1', _('house')), ('2', _('shop'))])
    room_count = CharField(max_length=2,
                                  choices=[('1', '1'), ('2', '2'),
                                          ('3', '3'), ('4', '>=4')])
    deck = CharField(max_length=2)
    acreage = IntegerField()
    loc_province = CharField(max_length=50)
    loc_city = CharField(max_length=50)
    loc_area = CharField(max_length=50)
    loc_cell = CharField(max_length=50)
    loc_addr = CharField(max_length=50)

    payee_name = CharField(max_length=255)
    payee_id_card = CharField(max_length=20)
    payee_bank = CharField(max_length=255)
    payee_bank_card = CharField(max_length=50)
    payee_bank_province = CharField(max_length=50)
    payee_bank_city = CharField(max_length=50)

    created_at = DateTimeField(auto_now=True)

    def pretty_name(self):
        """Return a beatifull name like: cellname|1 room| hight| 123m2"""
        return '|'.join(self.loc_cell, self.room_count,
                        self.deck, self.acreage)


class LandlordRenterInfo(Model, BaseModel):
    """A Landlord can have many renter. Each renter pay difference expense."""
    rent = ForeignKey(LandlordRentProfile)
    renter = ForeignKey(User)

    renter_name = CharField(max_length=255)
    rent_expense = IntegerField()
    rent_months = IntegerField()
    rent_begin_date = DateField()
    rent_pay_model = CharField(max_length=2, choices=[
        ('1', 'one month'), ('2', 'three month'),
        ('4', 'six month'), ('8', 'twenty month')])
    pay_months = IntegerField()
    pay_begin_date = DateField()
    deposit = IntegerField()
    arrive_type = CharField(max_length=2, choices=[
        ('1', 'next day'), ('2', 'two hours')])
    i_pay_it = BooleanField()

    service_expense = IntegerField()
    total_expense = IntegerField()
    created_at = DateTimeField(auto_now=True)

    state = CharField(max_length=2, choices=[('1', 'NoPay'), ('2', 'Verify'),
                                             ('3', 'VerifyPassed'),
                                             ('4', 'VerifyFailed'),
                                             ('5', 'Canceled')])


class RenterRentProfile(Model, BaseModel):
    """A renter can rent many house."""
    renter = ForeignKey(User)

    rent_type = CharField(max_length=2,
                                 choices=[(1, 'house'), (2, 'shop')])
    room_count = CharField(max_length=2,
                                  choices=[(1, '1'), (2, '2'),
                                          (3, '3'), (4, '>=4')])
    deck = CharField(max_length=2)
    acreage = IntegerField()

    rent_expense = IntegerField()
    rent_months = IntegerField()
    rent_begin_date = DateField()

    loc_province = CharField(max_length=50)
    loc_city = CharField(max_length=50)
    loc_area = CharField(max_length=50)
    loc_cell = CharField(max_length=50)
    loc_addr = CharField(max_length=50)

    payee_type = CharField(max_length=2, choices=[
        (1, 'person'), (2, 'company')])
    payee_name = CharField(max_length=255)
    payee_bank = CharField(max_length=255)
    payee_bank_card = CharField(max_length=50)
    payee_bank_province = CharField(max_length=50)
    payee_bank_city = CharField(max_length=50)
    payee_phone = CharField(max_length=30)


class RenterOption(Model, BaseModel):
    """A RenterRentProfile can only have one RenterOption"""
    rent_profile = OneToOneField(RenterRentProfile)

    pay_months = IntegerField()
    pay_begin_data = DateField()
    total_expense = IntegerField()
    deposit = IntegerField()
    comment = CharField(max_length=255)
    arrive_type = CharField(max_length=2, choices=[
        (1, 'next day'), (2, 'two hours')])
    is_installment = BooleanField()

    service_expense = IntegerField()
    created_at = DateTimeField(auto_now=True)

    state = CharField(max_length=2, choices=[(1, 1), (2, 2), (3, 3),
                                             (4, 4), (5, 5)])

    confirmed = BooleanField()


class Message(Model, BaseModel):
    """User messages. A User will have many message to him"""
    owner = ForeignKey(User)
    content = CharField(max_length=255)
    created_at = DateTimeField(auto_now=True)
    is_readed = BooleanField()


class BankCard(Model, BaseModel):
    """A user will have many bank card."""
    owner = ForeignKey(User)
    bank_name = CharField(max_length=50)
    card_user_name = CharField(max_length=255)
    card_no = CharField(max_length=50)
    card_loc = CharField(max_length=255)

    deleted = BooleanField()
