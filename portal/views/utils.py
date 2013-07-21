# -*- coding: utf-8 -*-
"""
Some helper function
"""
import urllib2
import smtplib
from email.mime.text import MIMEText

from django.shortcuts import render_to_response

from portal import models


def render(template_name, payment):
    return render_to_response('portal/%s' % template_name, payment)


def set_session(request, username):
    request.session['username'] = username


def unset_session(request, username):
    del request.session['username']


def get_user_obj(request):
    """Since the method is invoked after require_auth(),
    so I assume 'username' always in session.
    """
    username = request.session.get('username')
    return models.User.objects.filter(username=username)[0]


def get_merchant_obj(request):
    """Since the method is invoked after require_auth(),
    so I assume 'merchant' always in session.
    """
    username = request.session.get('username')
    return models.Merchant.objects.filter(username=username)[0]


def send_mail(receiver, content):
    sender = 'smartbrandnew@163.com'  # 'server'
    subject = 'activation mail'
    username = 'smartbrandnew'
    password = 'cqmd53603114'
    msg = MIMEText(content, 'html', 'utf-8')
    msg['Subject'] = subject
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


def send_msg(receiver, content):
    url = 'http://www.uoleem.com.cn/api/uoleemApi?username=suncong&pwd=suncong&mobile=' + str(receiver) + '&content=' + content
    url2 = 'http://utf8.sms.webchinese.cn/?Uid=smartbrandnew&Key=841092&smsMob=' + str(receiver) + '&smsText=' + content
    res = urllib2.urlopen(url)
