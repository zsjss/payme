# -*- coding: utf-8 -*-

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


URL_PREFIX = '/z/'


class UrlTestCase(TestCase):

    def test_200_url(self):
        """Make sure all url works."""
        urls = [
            '/',
            'signin/',
            'signup/',
            'logout/',
            'chargerent/',
            'chargerent/1/',
            'chargerent/1/update/',
            'chargerent/1/addrenter/',
            'chargerent/1/addrenter/1/confirm/',
            'chargerent/1/addrenter/1/done/',
            'chargerent/1/renter/1/cancel/',
            'account/',
            'account/payrentlist/',
            'account/chargerentlist/',
            'account/payments/',
            'account/safe/',
            'account/info/',
            'account/cardmanage/',
            'account/vip/',
        ]

        for url in urls:
            url = URL_PREFIX + url
            resp = self.client.get(url, follow=True)
            self.assertEqual(200, resp.status_code,
                             '%s != %s, path: %s, %s' %
                             (200, resp.status_code, url, resp.content))
