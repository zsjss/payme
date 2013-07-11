# -*- coding: utf-8 -*-
"""
The Merchant Account here.

For example: Merchant Home House , etc.
"""

from portal.views.merchantbase import mer_require_auth
from portal.views import utils
from django.views import generic
from portal import forms
from portal import models



@mer_require_auth
def merchanthome(request):
    return utils.render('merchant/home.html',{'welcome': 'Welcome'})


@mer_require_auth
def ordermanage(request):
    pass


@mer_require_auth
def housemanage(request):
    merchant = utils.get_merchant_obj(request)
    #merchant_id = merchant.id
    #house = models.House.objects.filter(owner_id=merchant_id)
    house = merchant.house_set.all()
    return utils.render('merchant/house.html', {'house':house})


class AddHouse(generic.FormView):
    
    template_name = 'portal/merchant/addhouse.html'
    form_class = forms.AddHouseForm
    
    def form_valid(self, form):
        merchant = utils.get_merchant_obj(self.request)
        form.instance.owner = merchant
        form.save()
        return housemanage(self.request)

addhouse = AddHouse.as_view()


@mer_require_auth
def merchantaccount(request):
    pass


@mer_require_auth
def merchantconfirm(request):
    pass




