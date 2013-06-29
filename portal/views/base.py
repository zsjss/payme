# -*- coding: utf-8 -*-

import functools

#from django import http
from . import render
from portal import forms
from portal import models


def check_authentication(func):
    """The decorator will check username and password from session.
    If the username and password is correct contiune.. otherwise redirect
    to sign_in page.
    """
    @functools.wraps(func)
    def _check_authentication(req):
        username = req.session.get('username')
        password = req.session.get('password')
        if username and password:
            user = models.User.object.filter(username=username)
            if password == user.password:
                # everything is ok, continue.
                func(req)
        #otherwise, redirect to signin page.
        return signin(req)

    return _check_authentication


def signin(req):
    """登陆"""
    return render('sign_in.html', {})


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


@check_authentication
def portal(req):
    return render('portal.html', {})


@check_authentication
def receive(req):
    pass


@check_authentication
def pay(req):
    pass
