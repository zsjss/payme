# -*- coding: utf-8 -*-
"""
The account views are here.
"""

from portal.views import utils
from portal.views.base import require_auth


@require_auth
def home(request):
    return utils.render('account/home.html', {})


@require_auth
def vip(request):
    return utils.render('account/vip.html', {})


@require_auth
def account_chargeent_list(request):
    user = utils.get_user_obj(request)
    charge_rents = user.landlordrentprofile_set.all()
    return utils.render('account/chargerentlist.html',
                        {'charge_rents': charge_rents})


@require_auth
def account_payrent_list(request):
    user = utils.get_user_obj(request)
    pay_rents = user.renterrentprofile_set.all()
    return utils.render('account/payrentlist.html',
                        {'pay_rents': pay_rents})


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
