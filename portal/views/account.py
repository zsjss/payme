# -*- coding: utf-8 -*-
"""
The account views are here.
"""

from portal.views import utils
from portal.views.base import check_authentication


@check_authentication
def home(req):
    return utils.render('account_home.html', {})


@check_authentication
def vip(req):
    return utils.render('vip.html', {})


@check_authentication
def cardmanage(req):
    pass


@check_authentication
def info(req):
    pass


@check_authentication
def safe(req):
    pass


@check_authentication
def messges(req):
    pass


@check_authentication
def payments(req):
    pass
