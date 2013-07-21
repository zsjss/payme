# -*- coding: utf-8 -*-
"""
The account views are here.
"""
import time
import logging
import functools
from django.core.exceptions import ValidationError

from django.shortcuts import redirect
from django.views import generic
from django.shortcuts import render_to_response

from portal import forms
from portal import models
from portal.views import utils
from portal.views.base import check_authentication

from portal.models import User

from PIL import Image
from DjangoVerifyCode import Code

import random


LOG = logging.getLogger(__name__)

@check_authentication
def verifycode(request):
    code = Code(request)
    code.worlds = ['hello','world','helloworld']
    code.type = 'number'
    return code.display()
   
@check_authentication	
def home(req):
    return utils.render('account_home.html', {})


@check_authentication
def vip(req):
    return utils.render('vip.html', {})


@check_authentication
def cardmanage(req):
    pass


@check_authentication
def info(req):
    usernam = req.session.get('username')
    user = models.User.objects.filter(username=usernam)
    return utils.render('personal_info.html',
                        {'username': user[0].username,
                         'phone': user[0].phone,
                         'real_id': user[0].real_id,
                         'real_name': user[0].real_name,
                         'email': user[0].email})	    
    


@check_authentication

def safe(req):
    usernam = req.session.get('username')
    user = models.User.objects.filter(username=usernam)
    local_time = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))
    return utils.render('security_certificate.html',
                        {'local_time': local_time,
                         'phone': user[0].phone})



@check_authentication
def headimg(req):
    pass


class NameCertification(generic.FormView):
    
    form_class = forms.NameCertificationForm
    template_name = 'portal/name_certificate.html'

    def form_valid(self, form):
        user = utils.get_user_obj(self.request)
        data = form.cleaned_data
        if user:
            user.real_name = data['real_name']
            user.real_id = data['real_id']
            user.save()
            return info(self.request)
        else:
        #LOG.debug("%s name certificate failed." % user)
            return utils.render('name_certificate.html',
                                {'errors': 'failed',
                                 'form': form})

namecertificate = NameCertification.as_view()

    
class PasswordModify(generic.FormView):

    form_class = forms.PasswordModifyForm
    template_name = 'portal/password_modify.html'

    def form_valid(self, form):
        user = utils.get_user_obj(self.request)
        data = form.cleaned_data
        if user and user.password == data['password'] and data['new_password'] == data['confirm_new_password']:
            user.password = data['new_password']
            user.save()
            return info(self.request)
        else:
        #LOG.debug("%s password modify failed." % user)
            return utils.render('password_modify.html',
                                {'errors': 'password is wrong',
                                 'form': form})

passwordmodify = PasswordModify.as_view()


class PhoneModify(generic.FormView):

    form_class = forms.PhoneModifyForm
    template_name = 'portal/phone_modify.html'
       
    def form_valid(self, form):
        user = utils.get_user_obj(self.request)
        data = form.cleaned_data
        print user.verifycode
        if user and data['phone'] and data['verification_code'] == str(user.verifycode):
            user.phone = data['phone']
            user.save()
            return safe(self.request)
        else:
        #LOG.debug("%s phone modify failed." % user)
            return utils.render('phone_modify.html',
                                {'errors': 'phone number is wrong',
                                 'form': form})

phonemodify = PhoneModify.as_view()


class SendVerifyCode(generic.FormView):
    
    form_class = forms.SendVerifyCodeForm
    template_name = 'portal/send_verifycode.html'
       
    def form_valid(self, form):
        user = utils.get_user_obj(self.request)
        data = form.cleaned_data
        if user and data['phone']:
            user.verifycode = random.randrange(0,999999)
            user.save()
            content = 'verifycode:' + str(user.verifycode)
            utils.send_msg(data['phone'], content)
            return phonemodify(self.request)
        else:
        #LOG.debug("%s phone modify failed." % user)
            return utils.render('send_verifycode.html',
                                {'errors': 'failed',
                                 'form': form})
    
sendverifycode = SendVerifyCode.as_view()


class MailboxModify(generic.FormView):
    
    form_class = forms.MailboxBindingForm
    template_name = 'portal/mailbox_binding.html'
    
    def form_valid(self, form):
        user = utils.get_user_obj(self.request)
        data = form.cleaned_data
        if user and data['email']:
            content = 'click here to active ' + '<a href="http://www.zufangbao.com/chargerent/">http://www.active.com</a>'
            utils.send_mail(data['email'], content)
            user.email = data['email']
            user.save()
            return safe(self.request)
        else:
        #LOG.debug("%s mailbox modify failed." % user)
            return utils.render('mailbox_modify.html',
                                {'errors': 'failed',
                                 'form': form})


mailboxbinding = MailboxModify.as_view()


class SecurityProblem(generic.FormView):
    
    form_class = forms.SecurityProblemForm
    template_name = 'portal/security_problem.html'
    
    def form_valid(self, form):
        user = utils.get_user_obj(self.request)
        data = form.cleaned_data
        if user and data['problem_one'] and data['problem_two'] and data['problem_three']:
            user.problem_one = data['problem_one']
            user.problem_two = data['problem_two']
            user.problem_three = data['problem_three']
            user.save()
            return safe(self.request)
        else:
        #LOG.debug("%s failed." % user)
            return utils.render('security_problem.html',
                                {'errors': 'failed',
                                 'form': form})


security_problem = SecurityProblem.as_view()






@check_authentication
def messges(req):
    pass


@check_authentication
def payments(req):
    pass
