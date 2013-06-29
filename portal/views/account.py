# -*- coding: utf-8 -*-

from portal.views.base import check_authentication


@check_authentication
def vip(req):
    pass


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


@check_authentication
def home(req):
    pass
