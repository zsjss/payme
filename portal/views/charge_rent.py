"""
All logic about charge rent.
"""
from django.views import generic
from django.shortcuts import redirect, get_object_or_404

from portal import models
from portal import forms
from portal.views import utils
from portal.views.base import require_auth


class ChargeRentCreateView(generic.FormView):

    form_class = forms.ChargeRentForm
    template_name = 'portal/charge/create.html'

    def form_valid(self, form):
        user = utils.get_user_obj(self.request)
        form.instance.landlord = user
        form.save()
        return redirect('charge_renter_add', form.instance.pk)

charge_rent_create = require_auth(ChargeRentCreateView.as_view())


class ChargeRentUpdateView(generic.FormView):

    form_class = forms.ChargeRentForm
    template_name = 'portal/charge/create.html'

    def get_initial(self):
        rent_id = self.args[0]
        assert rent_id
        x = get_object_or_404(models.LandlordRentProfile, pk=rent_id)
        return x.as_dict()

    def form_valid(self, form):
        rent_id = self.args[0]
        assert rent_id
        x = get_object_or_404(models.LandlordRentProfile, pk=rent_id)
        x.update_from_dict(form.cleaned_data)
        x.save()
        return redirect('charge_rent_detail', x.id)

charge_rent_update = require_auth(ChargeRentUpdateView.as_view())


class ChargeRenterCreateView(generic.FormView):
    """
    :rent_id: charge rent profile id.
    """

    form_class = forms.ChargeRenterForm
    template_name = 'portal/charge/renter_add.html'

    def form_valid(self, form):
        rent_id = self.args[0]
        assert rent_id
        rent = get_object_or_404(models.LandlordRentProfile, pk=rent_id)

        renter = models.LandlordRenterInfo(**form.cleaned_data)
        renter.rent = rent
        #TODO: Calucate service expense
        renter.service_expense = 0
        renter.total_expense = renter.rent_months * renter.rent_expense
        renter.state = '0'
        renter.save()
        return redirect('charge_renter_confirm', rent.id, renter.id)

charge_renter_add = require_auth(ChargeRenterCreateView.as_view())


def charge_rent_detail(request, profile_id):
    rent = get_object_or_404(models.LandlordRentProfile, pk=profile_id)
    return utils.render('charge/detail.html', {'rent': rent})


def charge_renter_confirm(request, rent_id, renter_id):
    renter = get_object_or_404(models.LandlordRenterInfo,
                               pk=renter_id, rent_id=rent_id)
    return utils.render('charge/renter_confirm.html',
                        {'renter': renter})


def charge_renter_done(request, rent_id, renter_id):
    renter = get_object_or_404(models.LandlordRenterInfo,
                               pk=renter_id, rent_id=rent_id)
    renter.state = '1'
    renter.save()
    return utils.render('charge/renter_finish.html', {})


def charge_renter_cancel(request, rent_id, renter_id):
    renter = get_object_or_404(models.LandlordRenterInfo,
                               pk=renter_id, rent_id=rent_id)
    renter.state = '5'
    renter.save()
    return redirect('charge_rent_detail', rent_id)
