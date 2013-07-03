# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from portal.views import base
from portal.views import charge_rent
from portal.views import pay_rent
from portal.views import account


urlpatterns = patterns('',
    url(r'^$', base.portal),
    url(r'^signin/', base.signin),
    url(r'^signup/', base.signup),
    url(r'^logout/', base.logout),
)

urlpatterns += patterns('',
    url(r'^chargerent/$', charge_rent.charge_rent_create),
    url(r'^chargerent/(\w+)/$', charge_rent.charge_rent_update),
    url(r'^chargerent/(\w+)/addrenter/$', charge_rent.charge_renter_add),
    url(r'^chargerent/(\w+)/addrenter/(\w+)/confirm$',
                                        charge_rent.charge_renter_confirm)
)

urlpatterns += patterns('',
    url(r'^payrent/$', pay_rent.pay_rent_profile_create),
    url(r'^payrent/(\w+)$', pay_rent.pay_rent_profile_update),
    url(r'^payrent/(\w+)/option', pay_rent.pay_rent_option_create),
    url(r'^payrent/(\w+)/optionedit', pay_rent.pay_rent_option_update),
)

urlpatterns += patterns('',
    url(r'^account/$', account.home),
    url(r'^account/payments/$', account.payments),
    url(r'^account/messges/$', account.messges),
    url(r'^account/safe/$', account.safe),
    url(r'^account/info/$', account.info),
    url(r'^account/cardmanage/$', account.cardmanage),
    url(r'^account/vip/$', account.vip),
)
