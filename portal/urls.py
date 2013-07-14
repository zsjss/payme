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

urlpatterns += patterns('portal.views.merchantbase',
    url(r'^merchant/signup/', 'merchsignup', name='merchant_signup'),
    url(r'^merchant/signin/', 'merchsignin', name='merchant_signin'),
    url(r'^merchant/logout/', 'merlogout', name='merchant_logout'),
)

urlpatterns += patterns('portal.views.merchantaccount',
    url(r'^merchant/home/', 'merchanthome', name='merchant_home'),
    url(r'^merchant/ordermanage/', 'ordermanage', name='merchant_ordermanage'),
    url(r'^merchant/housemanage/', 'housemanage', name='merchant_housemanage'),
    url(r'^merchant/addhouse/', 'addhouse', name='merchant_addhouse'),
    url(r'^merchant/account/', 'merchantaccount', name='merchant_account'),
    url(r'^merchant/confirm/', 'merchantconfirm', name='merchant_confirm'),
    url(r'^merchant/changepassword/', 'changepassword', name='changepassword'),
    url(r'^merchant/rentalaccount/', 'rentalaccount', name='rentalaccount'),
    url(r'^merchant/addrentalaccount/', 'addrentalaccount', name='addrentalaccount'),
    url(r'^merchant/money/', 'accountmoney', name='account_money'),
    url(r'^merchant/addmoney/', 'addaccountmoney', name='addaccountmoney'),
    url(r'^merchant/message/', 'merchantmessage', name='merchant_message'),
)








