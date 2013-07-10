# -*- coding: utf-8 -*-
"""
The Merchant basic view logic here.

For example: Merchant signin, signup, homepage , etc.
"""

import logging
import functools

from django.shortcuts import redirect
from django.views import generic

from portal import forms
from portal import models
from portal.views import utils
from portal.views.base import require_auth

LOG = logging.getLogger(__name__)


def mer_require_auth(func):
    """The decorator will check username existed in session. If it is continue.
    """
    @functools.wraps(func)
    def _mer_require_auth(request, *args, **kwargs):
        username = request.session.get('username')
        if not username:
            return merchsignin(request, *args, **kwargs)
        else:
            return func(request, *args, **kwargs)

    return _mer_require_auth


class MerchSignIn(generic.FormView):
    
    form_class = forms.SignInForm
    template_name = 'portal/merchant/m_sign_in.html'
    
    def form_valid(self, form):
        data = form.cleaned_data
        users = models.Merchant.objects.filter(username=data['username'])
        if users and users[0].password == data['password']:
            LOG.debug('%s login success.' % users)
            utils.set_session(self.request, users[0].username)
            return utils.render('merchant/house.html', {})
        else:
            LOG.debug('%s login failed.' % users)
            return utils.render('merchant/m_sign_in.html',
                                {'error': 'Username or password is wrong!',
                                 'form':form})
    
merchsignin = MerchSignIn.as_view()


class MerchSignUp(generic.FormView):
    
    template_name = 'portal/merchant/m_sign_up.html'
    form_class = forms.MerchSignUpForm
    
    def form_valid(self, form):
        data = form.cleaned_data
        user = models.Merchant(**data)
        user.save()
        return utils.render('merchant/house.html', {})
    
merchsignup = MerchSignUp.as_view()


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
def housemanage(request):
    merchant = utils.get_merchant_obj(request)
    #merchant_id = merchant.id
    #house = models.House.objects.filter(owner_id=merchant_id)
    house = merchant.house_set.all()
    return utils.render('merchant/house.html', {'house':house})
    

    


