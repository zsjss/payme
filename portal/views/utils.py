# -*- coding: utf-8 -*-
"""
Some helper function
"""

from django.shortcuts import render_to_response

from portal import models

import smtplib 
from email.mime.text import MIMEText

def render(template_name, payment):
    return render_to_response('portal/%s' % template_name,
                              payment)


def set_session(req, username):
    req.session['username'] = username


def unset_session(req, username):
    del req.session['username']


def get_user_obj(req):
    """Since the method is invoked after check_authentication(),
    so I assume 'username' always in session.
    """
    username = req.session.get('username')
    print username
    return models.User.objects.filter(username=username)[0]

def send_mail(receiver, content):
    
    sender = 'smartbrandnew@163.com' #'server'
    subject = 'activation mail'
    smtpserver = 'smtp.163.com'
    username = 'smartbrandnew'
    password = 'cqmd53603114'
    msg = MIMEText(content,'html','utf-8') 
    msg['Subject'] = subject
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
