# -*- coding: utf-8 -*-
"""
The basic view logic here.

For example: signin, signup, homepage , etc.
"""

import logging
import functools

from django.shortcuts import redirect
from django.views import generic

from portal import forms
from portal import models
from portal.views import utils

LOG = logging.getLogger(__name__)


def require_auth(func):
    """The decorator will check username existed in session. If it is continue.
    """
    @functools.wraps(func)
    def _require_auth(request, *args, **kwargs):
        username = request.session.get('username')
        if not username:
            return signin(request, *args, **kwargs)
        else:
            return func(request, *args, **kwargs)

    return _require_auth


class SignIn(generic.FormView):

    form_class = forms.SignInForm
    template_name = 'portal/sign_in.html'

    def form_valid(self, form):
        data = form.cleaned_data
        users = models.User.objects.filter(username=data['username'])
        if users and users[0].password == data['password']:
            LOG.debug('%s login success.' % users)
            utils.set_session(self.request, users[0].username)
            return portal(self.request)
        else:
            LOG.debug("%s login failed." % users)
            return utils.render('sign_in.html',
                                {'errors': 'Username or password is wrong',
                                 'form': form})

signin = SignIn.as_view()


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


class SignUp(generic.FormView):

    template_name = 'portal/sign_up.html'
    form_class = forms.SignUpForm

    def form_valid(self, form):
        data = form.cleaned_data
        user = models.User(**data)
        user.save()
        return utils.render('portal.html', {})

signup = SignUp.as_view()


class MerchSignUp(generic.FormView):
    template_name = 'portal/merchant/m_sign_up.html'
    form_class = forms.MerchSignUpForm
    
    def form_valid(self, form):
        data = form.cleaned_data
        user = models.Merchant(**data)
        user.save()
        return utils.render('merchant/m_base.html', {})
    
merchsignup = MerchSignUp.as_view()


@require_auth
def portal(request):
    user = utils.get_user_obj(request)
    return utils.render('portal.html', {})


class ChargeRent(generic.FormView):
    form_class = forms.ChargeRentForm
    template_name = 'portal/charge_rent.html'

    def form_valid(self, form):
        data = form.cleaned_data
        me = utils.get_user_obj(self.request)
        house = models.House(owner=me,
                             house_name=data['location_area'],
                             house_size=int(data['house_size']))
        house.save()
        return portal(self.request)

chargerent = require_auth(ChargeRent.as_view())


@require_auth
def logout(request):
    username = request.session['username']
    utils.unset_session(request, username)
    return portal(request)
