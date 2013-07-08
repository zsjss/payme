# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns('portal.views.base',
    url(r'^$', 'portal', name='portal'),
    url(r'^signin/', 'signin', name='signin'),
    url(r'^signup/', 'signup', name='signup'),
    url(r'^logout/', 'logout', name='logout'),   
)

urlpatterns += patterns('portal.views.charge_rent',
    url(r'^chargerent/$',
                    'charge_rent_create', name='charge_rent_create'),
    url(r'^chargerent/(\w+)/$',
                    'charge_rent_update', name='charge_rent_update'),
    url(r'^chargerent/(\w+)/addrenter/$',
                    'charge_renter_add', name='charge_renter_add'),
    url(r'^chargerent/(\w+)/addrenter/(\w+)/confirm$',
                    'charge_renter_confirm', name='charge_renter_confirm'),
    url(r'^chargerent/(\w+)/addrenter/(\w+)/done$',
                    'charge_renter_done', name='charge_renter_done'),
)

urlpatterns += patterns('portal.views.pay_rent',
    url(r'^payrent/$',
                'pay_rent_profile_create', name='pay_rent_profile_create'),
    url(r'^payrent/(\w+)$',
                'pay_rent_profile_update', name='pay_rent_profile_update'),
    url(r'^payrent/(\w+)/option',
                'pay_rent_option_create', name='pay_rent_option_create'),
    url(r'^payrent/(\w+)/optionedit',
                'pay_rent_option_update', name='pay_rent_option_update'),
)

urlpatterns += patterns('portal.views.account',
    url(r'^account/$', 'home', name='home'),
    url(r'^account/payments/$', 'payments', name='account_payments'),
    url(r'^account/messages/$', 'messages', name='account_messages'),
    url(r'^account/safe/$', 'safe', name='account_safe'),
    url(r'^account/info/$', 'info', name='account_info'),
    url(r'^account/cardmanage/$', 'cardmanage', name='account_cardmamage'),
    url(r'^account/vip/$', 'vip', name='account_vip'),  
)

urlpatterns += patterns('portal.views.merchant',
    url(r'^merchant/signup/', 'merchsignup', name='merchant_signup'),
    url(r'^merchant/signin/', 'merchsignin', name='merchant_signin'),
)