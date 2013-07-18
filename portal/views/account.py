# -*- coding: utf-8 -*-
"""
The account views are here.
"""

from portal.views import utils
from portal.views.base import require_auth
from portal.models import User
from portal.models import Message, BankCard
from django.views import generic
from portal import forms
from portal import models

@require_auth
def home(request):
    return utils.render('account_home.html', {})


@require_auth
def vip(request):
    user = utils.get_user_obj(request)
    
    if user.is_vip == False:
        return vipconfirm(request)
    else:
        return utils.render('account/vip.html', {'message': 'Welcome,VIP!'})


class Vipconfirm(generic.FormView):
    template_name = 'portal/account/vipconfirm.html'
    form_class = forms.VipForm
    
    def form_valid(self, form):
        user = utils.get_user_obj(self.request)
        data = form.cleaned_data
        if models.Vip.objects.filter(text=data['text']):
            user.is_vip = True
            user.save()
            return vip(self.request)

vipconfirm = Vipconfirm.as_view()
        
        
@require_auth
def cardmanage(request):
    user = utils.get_user_obj(request)
    #user_id = user.id
    #cards = BankCard.objects.filter(owner_id = user_id)
    cards = user.bankcard_set.all()
    return utils.render('account/bankcards.html',{'cards': cards})


@require_auth
def info(request):
    pass


@require_auth
def safe(request):
    pass


@require_auth
def messages(request):
    user = utils.get_user_obj(request)
    #user_id = user.id
    #message = Message.objects.filter(owner_id = user_id)
    message = user.message_set.all()
    return utils.render('account/account_messages.html',{'message': message})


@require_auth
def payments(request):
    pass
