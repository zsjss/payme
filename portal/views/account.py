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
    username = request.session.get('username')
    user = User.objects.filter(username = username)
    user_id = user[0].id
    message = Message.objects.filter(owner_id = user_id)
    return utils.render('account_messages.html',{'message': message})


@require_auth
def payments(request):
    pass
