# -*- coding: utf-8 -*-
"""
The basic view logic here.

For example: signin, signup, homepage , etc.
"""

import functools
import logging

#from django import http
from . import render
from portal import forms
from portal import models

LOG = logging.getLogger(__name__)


def check_authentication(func):
    """The decorator will check username existed in session. If it is continue.
    """
    @functools.wraps(func)
    def _check_authentication(req):
        username = req.session.get('username')
        if not username:
            return signin(req)
        else:
            func(req)

    return _check_authentication


def _set_session(req, username):
    req.session['username'] = username


def signin(req):
    """登陆"""
    if req.method == 'GET':
        form = forms.SignInForm()
        return render('sign_in.html', {'form': form})
    elif req.method == 'POST':
        form = forms.SignInForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = models.User.objects.filter(username=data['username'])[0]
            if user.password == data['password']:
                LOG.debug('%s login success.' % user)
                _set_session(req, user.username)
                return portal(req)
            else:
                LOG.debug("%s login failed." % user)
                return render('sign_in.html',
                                {'errors': 'Username or password wrong',
                                 'form': form})
        else:
            return render('sign_in.html', {'form': form})


def signup(req):
    """注册"""
    if req.method == 'GET':
        form = forms.SignUpForm()
        return render('sign_up.html', {'form': form})
    elif req.method == 'POST':
        form = forms.SignUpForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = models.User(**data)
            user.save()
            return render('portal.html', {})
        else:
            return render('sign_up.html', {'form': form})


def portal(req):
    return render('portal.html', {})


@check_authentication
def receive(req):
    pass


@check_authentication
def pay(req):
    pass
