# -*- coding: utf-8 -*-
"""
Database models are defined here.
"""

from django.db.models import Model
from django.db.models import IntegerField, CharField, DateTimeField
from django.db.models import DateField, EmailField, BooleanField, ImageField
from django.db.models import ForeignKey, OneToOneField
from django.contrib import admin
from PIL import Image
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_unicode

class BaseModel(object):
    pass


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
    front_image = ImageField(upload_to='upload')
    back_image = ImageField(upload_to='upload')
    problem_one = CharField(max_length=255)
    problem_two = CharField(max_length=255)
    problem_three = CharField(max_length=255)
    verifycode = CharField(max_length=255)
    



class UserAdmin(admin.ModelAdmin):
    list_display = ['username']


##################################
class LandlordRentProfile(Model, BaseModel):
    """A user who is landlord can have many rent."""
    landlord = ForeignKey(User)

    rent_type = CharField(max_length=2,
                                 choices=[(1, 'house'), (2, 'shop')])
    room_count = CharField(max_length=2,
                                  choices=[(1, '1'), (2, '2'),
                                          (3, '3'), (4, '>=4')])
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


class LandlordRenterInfo(Model, BaseModel):
    """A Landlord can have many renter. Each renter pay difference expense."""
    rent = ForeignKey(LandlordRentProfile)
    renter = ForeignKey(User)

    renter_name = CharField(max_length=255)
    rent_expense = IntegerField()
    rent_monthsn = IntegerField()
    rent_begin_date = DateField()
    rent_pay_model = CharField(max_length=2, choices=[
        (1, 'one month'), (2, 'three month'),
        (4, 'six month'), (8, 'twenty month')])
    pay_months = IntegerField()
    pay_begin_date = DateField()
    deposit = IntegerField()
    arrive_type = CharField(max_length=2, choices=[
        (1, 'next day'), (2, 'two hours')])
    i_pay_it = BooleanField()

    service_expense = IntegerField()
    total_expense = IntegerField()
    created_at = DateTimeField(auto_now=True)

    state = CharField(max_length=2, choices=[(1, 1), (2, 2), (3, 3),
                                             (4, 4), (5, 5)])


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
    
    
class PayOrder(models.Model):
    username = models.CharField(max_length=128, db_index=True, verbose_name=_('Username'))
    user_id = models.CharField(blank=True, null=True, max_length=64, verbose_name=_('UserID'))
    tenant_id  = models.CharField(blank=True, null=True, max_length=64, verbose_name=_('TenantID '))
    goods_name = models.CharField(max_length=256, verbose_name=_('Goods Name'))
    order_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Created Time'))
    trade_no = models.CharField(max_length=128, unique=True, verbose_name=_('Out Trade Number'))
    total_fee = models.IntegerField(max_length=64, verbose_name=_('Total Fee'))
    transaction_id = models.CharField(blank=True, null=True, max_length=128, verbose_name=_('Transaction ID'))
    trade_state = models.IntegerField(blank=True, null=True, max_length=1, verbose_name=_('Trade State'))
    trade_mode = models.IntegerField(blank=True, null=True, max_length=1, verbose_name=_('Trade Mode'))
    pay_info = models.CharField(blank=True, null=True, max_length = 128, verbose_name=_('Pay Info'))
    ret_code = models.CharField(blank=True, null=True, max_length = 8, verbose_name=_('Return Info'))
    ret_msg = models.CharField(blank=True, null=True, max_length = 256, verbose_name=_('Return Message'))
    send_sms = models.BooleanField(verbose_name = _('Send Sms To User'))
    requrl = models.CharField(blank=True, null=True, max_length=1024,verbose_name = _('Payment Reques URL'))
    
    payment_choice = (
        (0,'NEW_ORDER'),
        (1,'PAYMENT'),
        (2,'MONEY_RECEIVED'),
    )
    payment_info = models.CharField(blank=True, null=True, max_length=8,choices=payment_choice,verbose_name=_('Payment Info'))
    
    def __unicode__(self):
        return smart_unicode('%s [%s] [%s]' % (self.username, self.order_date, self.goods_name))
    
    class Meta:
        verbose_name = _('PayOrder')
        verbose_name_plural = _('PayOrder')
        ordering = ['-order_date']
