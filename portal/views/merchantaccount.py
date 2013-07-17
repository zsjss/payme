# -*- coding: utf-8 -*-
"""
The Merchant Account here.

For example: Merchant Home House , etc.
"""

import logging
from portal.views.merchantbase import mer_require_auth
from portal.views import utils
from django.views import generic
from portal import forms
from portal import models
from portal.alipay import alipay
import random

LOG = logging.getLogger(__name__)

@mer_require_auth
def merchanthome(request):
    return utils.render('merchant/home.html',{'welcome': 'Welcome'})


@mer_require_auth
def ordermanage(request):
    pass


@mer_require_auth
def housemanage(request):
    merchant = utils.get_merchant_obj(request)
    #merchant_id = merchant.id
    #house = models.House.objects.filter(owner_id=merchant_id)
    house = merchant.house_set.all()
    return utils.render('merchant/house.html', {'house':house})


class AddHouse(generic.FormView):
    
    template_name = 'portal/merchant/addhouse.html'
    form_class = forms.AddHouseForm
    
    def form_valid(self, form):
        merchant = utils.get_merchant_obj(self.request)
        form.instance.owner = merchant
        form.save()
        return housemanage(self.request)

addhouse = AddHouse.as_view()


@mer_require_auth
def merchantaccount(request):
    merchant = utils.get_merchant_obj(request)
    return utils.render('merchant/accountmanage.html', {'username': merchant.username,
                                                        'real_name': merchant.real_name,
                                                        'phone': merchant.phone})


class ChangePassword(generic.FormView):
    
    template_name = 'portal/merchant/changepassword.html'
    form_class = forms.ChangePasswordForm
    
    def form_valid(self, form):
        merchant = utils.get_merchant_obj(self.request)
        data = form.cleaned_data
        if merchant and merchant.password == data['oldpassword'] and data['newpassword'] == data['newpassagain']:
            merchant.password = data['newpassword']
            merchant.save()
            return merchantaccount(self.request)
        else:
            LOG.debug("%s Change password failed." %merchant )
            return utils.render('merchant/changepassword.html',
                                {'errors': 'Password is wrong',
                                 'form': form})

changepassword = ChangePassword.as_view()


@mer_require_auth
def merchantconfirm(request):
    pass


@mer_require_auth
def rentalaccount(request):
    merchant = utils.get_merchant_obj(request)
    rentalaccount = merchant.rentalaccount_set.all()
    return utils.render('merchant/rentalaccount.html', {'rentalaccount': rentalaccount})


class AddRentalAccount(generic.FormView):
    
    template_name = 'portal/merchant/addrentalaccount.html'
    form_class = forms.AddRentalAccountForm
    
    def form_valid(self, form):
        merchant = utils.get_merchant_obj(self.request)
        form.instance.owner = merchant
        form.save()
        return rentalaccount(self.request)
    
addrentalaccount = AddRentalAccount.as_view()


@mer_require_auth
def accountmoney(request):
    merchant = utils.get_merchant_obj(request)
    money = merchant.accountmoney_set.all()
    #totalmoney = models.TotalMoney.objects.filter(owner_id=merchant.id)
    totalmoney = 0.0
    for m in money:
        totalmoney += m.in_out_money
    return utils.render('merchant/accountmoney.html', {'totalmoney': totalmoney,
                                                       'money': money})


class AddAccountMoney(generic.FormView):
    template_name = 'portal/merchant/addmoney.html'
    form_class = forms.AddAccountMoneyForm
    
    def form_valid(self, form):
        merchant = utils.get_merchant_obj(self.request)
        #form.instance.owner = merchant
        #form.save()
        #return accountmoney(self.request)
        data = form.cleaned_data
        tn = random.uniform(1,100)
        if alipay.create_direct_pay_by_user(tn, data['pay_type'], data['operation_name'], data['in_out_money']):
            form.instance.owner = merchant
            form.save()
        return utils.render('merchant/paysuccess.html', {})

addaccountmoney = AddAccountMoney.as_view()


@mer_require_auth
def merchantmessage(request):
    merchant = utils.get_merchant_obj(request)
    message = merchant.merhantmessage_set.all()
    return utils.render('merchant/merchantmessage.html',{'message': message})


