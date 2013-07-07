# -*- coding: utf-8 -*-
"""
The account views are here.
"""

from portal.views import utils
from portal.views.base import require_auth
from portal.models import User
from portal.models import Message, BankCard


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

    renters = []
    passive_renters = user.landlordrenterinfo_set.all()
    active_renters = user.renterrentprofile_set.all()

    renters.extend(passive_renters)
    renters.extend(active_renters)
    renters.sort(key=lambda x: x.created_at)
    renters.reverse()
    return utils.render('account/payrentlist.html',
                        {'renters': renters})


@require_auth
def cardmanage(request):
    user = utils.get_user_obj(request)
    #user_id = user.id
    #cards = BankCard.objects.filter(owner_id = user_id)
    cards = user.bankcard_set.all()
    return utils.render('bankcards.html',{'cards': cards})


@require_auth
def info(request):
    pass


@require_auth
def safe(request):
    pass


@require_auth
def messges(request):
    user = utils.get_user_obj(request)
    #user_id = user.id
    #message = Message.objects.filter(owner_id = user_id)
    message = user.message_set.all()
    return utils.render('account_messages.html',{'message': message})


@require_auth
def payments(request):
    pass
