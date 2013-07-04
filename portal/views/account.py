# -*- coding: utf-8 -*-
"""
The account views are here.
"""

from portal.views import utils
from portal.views.base import require_auth


@require_auth
def home(request):
    return utils.render('account_home.html', {})


@require_auth
def vip(request):
    return utils.render('vip.html', {})


@require_auth
def cardmanage(request):
    pass


@require_auth
def info(request):
    pass


@require_auth
def safe(request):
    pass


@require_auth
def messges(request):
    pass


@require_auth
def payments(request):
    pass
