# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns('portal.views.base',
    url(r'^$', 'portal', name='portal'),
    url(r'^signin/', 'signin', name='signin'),
    url(r'^signup/', 'signup', name='signup'),
    url(r'^pay/', 'pay', name='pay'),
    url(r'^receive/', 'receive', name='receive'),
)

urlpatterns += patterns('portal.views.account',
    url(r'^account/$', 'home', name='home'),
    url(r'^account/payments$', 'payments', name='account_payments'),
    url(r'^account/messges$', 'messges', name='account_messges'),
    url(r'^account/safe$', 'safe', name='account_safe'),
    url(r'^account/info$', 'info', name='account_info'),
    url(r'^account/cardmanage$', 'cardmanage', name='account_cardmamage'),
    url(r'^account/vip$', 'vip', name='account_vip'),
)
