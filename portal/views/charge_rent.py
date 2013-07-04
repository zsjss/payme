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
        return redirect('portal')

charge_rent_update = require_auth(ChargeRentUpdateView.as_view())


class ChargeRentCreateView(generic.FormView):

    form_class = forms.ChargeRenterForm
    template_name = 'portal/charge/renter_add.html'

    def form_valid(self, form):
        rent_id = self.args[0]
        assert rent_id
        #TODO: save renter info into databse.
        return redirect('charge_renter_confirm', 'hehe', 'haha')

charge_renter_add = require_auth(ChargeRentCreateView.as_view())


def charge_renter_confirm(request, profile_id, renter_info_id):
    #TODO:
    return utils.render('charge/renter_confirm.html',
                        {'rent_id': profile_id,
                         'renter_id': renter_info_id})


def charge_renter_done(request, profile_id, renter_info_id):
    #TODO:
    return utils.render('charge/renter_finish.html', {})
