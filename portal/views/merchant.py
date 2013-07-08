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

LOG = logging.getLogger(__name__)


class MerchSignIn(generic.FormView):
    
    form_class = forms.SignInForm
    template_name = 'portal/merchant/m_sign_in.html'
    
    def form_valid(self, form):
        data = form.cleaned_data
        users = models.Merchant.objects.filter(username=data['username'])
        if users and users[0].password == data['password']:
            LOG.debug('%s login success.' % users)
            utils.set_session(self.request, users[0].username)
            return utils.render('merchant/m_base.html', {})
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
        return utils.render('merchant/m_base.html', {})
    
merchsignup = MerchSignUp.as_view()