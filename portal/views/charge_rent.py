"""
All logic about charge rent.
"""
from django.views import generic
from django.shortcuts import redirect

from portal import forms
from portal.views import utils
from portal.views.base import check_authentication


class ChargeRentCreateView(generic.FormView):

    form_class = forms.ChargeRentForm
    template_name = 'portal/charge/create.html'

    def form_valid(self, form):
        return redirect('charge_renter_add', 'hehe')

charge_rent_create = check_authentication(ChargeRentCreateView.as_view())


def charge_rent_update(request, profile_id):
    pass


class ChargeRentCreateView(generic.FormView):

    form_class = forms.ChargeRenterForm
    template_name = 'portal/charge/renter_add.html'

    def form_valid(self, form):
        rent_id = self.args[0]
        assert rent_id
        return redirect('charge_renter_confirm', 'hehe', 'haha')

charge_renter_add = check_authentication(ChargeRentCreateView.as_view())


def charge_renter_confirm(request, profile_id, renter_info_id):
    return utils.render('charge/renter_confirm.html',
                        {'rent_id': profile_id,
                         'renter_id': renter_info_id})


def charge_renter_done(request, profile_id, renter_info_id):
    return utils.render('charge/renter_finish.html', {})
