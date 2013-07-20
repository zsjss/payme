"""
All logic about pay rent.
"""
from django import http
from django.views import generic
from django.shortcuts import redirect, get_object_or_404

from portal import models
from portal import forms
from portal.views import utils
from portal.views.base import require_auth


class PayRentCreateView(generic.FormView):

    form_class = forms.ChargeRentForm
    template_name = 'portal/payrent/create.html'

    def form_valid(self, form):
        user = utils.get_user_obj(self.request)
        form.instance.renter = user
        form.save()
        return redirect('charge_renter_add', form.instance.pk)
pay_rent_profile_create = require_auth(PayRentCreateView.as_view())


def pay_rent_profile_update(request, profile_id):
    pass


def pay_rent_option_create(request, profile_id):
    pass


def pay_rent_option_update(request, profile_id):
    pass


def pay_rent_payit(request, rent_uuid):
    return http.HttpResponse('pay it Not Implemented.')


def pay_rent_detail(request, rent_uuid):
    try:
        renter = models.LandlordRenterInfo.objects.get(uuid=rent_uuid)
        return utils.render('pay/detail_landlord.html',
                     {'renter': renter})
    except models.LandlordRenterInfo.DoesNotExist:
        # Else use an renter detail template
        renter = get_object_or_404(models.RenterRentProfile, uuid=rent_uuid)
        return utils.render('pay/detail_renter.html',
                     {'renter': renter})


def pay_rent_cancel(request, rent_uuid):
    pass
