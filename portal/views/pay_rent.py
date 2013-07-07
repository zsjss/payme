"""
All logic about pay rent.
"""
from django import http
from django.shortcuts import redirect, get_object_or_404

from portal import models
from portal.views import utils
from portal.views.base import require_auth


def pay_rent_profile_create(request):
    pass


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
