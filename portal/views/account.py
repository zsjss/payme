# -*- coding: utf-8 -*-
"""
The account views are here.
"""

from portal.views import utils
from portal.views.base import check_authentication


@check_authentication
def home(request):
    return utils.render('account_home.html', {})


@check_authentication
def vip(request):
    return utils.render('vip.html', {})


@check_authentication
def cardmanage(request):
    pass


@check_authentication
def info(request):
    pass


@check_authentication
def safe(request):
    pass


@check_authentication
def messges(request):
    pass


@check_authentication
def payments(request):
    pass
