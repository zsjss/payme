# -*- coding: utf-8 -*-
"""
The account views are here.
"""
import time
import logging
import random

from django.views import generic


#from DjangoVerifyCode import Code

from portal import forms
from portal import models
from portal.views import utils
from portal.views.base import require_auth
from portal.views.base import sendmessage

LOG = logging.getLogger(__name__)


@require_auth
def home(request):
    return utils.render('account/home.html', {})


@require_auth
def verifycode(request):
    code = Code(request)
    code.worlds = ['hello', 'world', 'helloworld']
    code.type = 'number'
    return code.display()


@require_auth
def vip(request):
    return utils.render('account/vip.html', {})


@require_auth
def account_chargeent_list(request):
    user = utils.get_user_obj(request)
    charge_rents = user.landlordrentprofile_set.all()
    return utils.render('account/chargerentlist.html',
                        {'charge_rents': charge_rents})


@require_auth
def account_payrent_list(request):
    user = utils.get_user_obj(request)

    renters = []
    passive_renters = user.landlordrenterinfo_set.all()
    active_renters = user.renterrentprofile_set.all()

    renters.extend(passive_renters)
    renters.extend(active_renters)
    renters.sort(key=lambda x: x.created_at)
    renters.reverse()
    return utils.render('account/payrentlist.html',
                        {'renters': renters})


@require_auth
def vip(request):
    user = utils.get_user_obj(request)

    if user.is_vip == False:
        return vipconfirm(request)
    else:
        return utils.render('account/vip.html', {'message': 'Welcome,VIP!'})


class Vipconfirm(generic.FormView):
    template_name = 'portal/account/vipconfirm.html'
    form_class = forms.VipForm

    def form_valid(self, form):
        user = utils.get_user_obj(self.request)
        data = form.cleaned_data
        if models.Vip.objects.filter(text=data['text']):
            user.is_vip = True
            user.save()
            content = 'You have been VIP client!'
            sendmessage(self.request, content)
            return vip(self.request)

vipconfirm = Vipconfirm.as_view()


@require_auth
def info(req):
    user = utils.get_user_obj(req)

    return utils.render('personal_info.html',
                        {'username': user.username,
                         'phone': user.phone,
                         'real_id': user.real_id,
                         'real_name': user.real_name,
                         'email': user.email,
                         'user': user})


@require_auth
def cardmanage(request):
    user = utils.get_user_obj(request)
    if models.BankCard.objects.filter(owner_id = user.id):
        cards = user.bankcard_set.all()
        return utils.render('account/bankcards.html', {'cards': cards})
    else:
        return addbankcards(request)


class Addbankcards(generic.FormView):
    template_name = 'portal/account/addbankcards.html'
    form_class = forms.AccountBankCardsForm
    
    def form_valid(self, form):
        user = utils.get_user_obj(self.request)
        form.instance.owner = user
        form.save()
        content = 'You have added a Bank Card Number!'
        sendmessage(self.request, content)
        return cardmanage(self.request)
    
addbankcards = require_auth(Addbankcards.as_view())
    


@require_auth
def safe(req):
    usernam = req.session.get('username')
    user = models.User.objects.filter(username=usernam)
    local_time = time.strftime('%Y-%m-%d-%H:%M:%S',
                               time.localtime(time.time()))
    return utils.render('security_certificate.html',
                        {'local_time': local_time,
                         'phone': user[0].phone})


class UploadPhoto(generic.FormView):
    template_name = 'portal/account/uploadphoto.html'
    form_class = forms.HeadImgForm
    
    def form_valid(self, form):
        user = utils.get_user_obj(self.request)
        data = form.cleaned_data
        user.photo = data['photo']
        user.save()
        return info(self.request)
    
uploadphoto = require_auth(UploadPhoto.as_view())


class NameCertification(generic.FormView):

    form_class = forms.NameCertificationForm
    template_name = 'portal/name_certificate.html'

    def form_valid(self, form):
        user = utils.get_user_obj(self.request)
        data = form.cleaned_data
        user.real_name = data['real_name']
        user.real_id = data['real_id']
        user.front_image = data['front_image']
        user.back_image = data['back_image']
        user.save()
        content = 'You have send personal information, please to wait for confirm!'
        sendmessage(self.request, content)
        return info(self.request)
        
namecertificate = require_auth(NameCertification.as_view())


class PasswordModify(generic.FormView):

    form_class = forms.PasswordModifyForm
    template_name = 'portal/password_modify.html'

    def form_valid(self, form):
        user = utils.get_user_obj(self.request)
        data = form.cleaned_data
        if user and user.password == data['password'] and \
           data['new_password'] == data['confirm_new_password']:
            user.password = data['new_password']
            user.save()
            content = 'Your password has been modified!'
            sendmessage(self.request, content)
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
        if user and data['phone'] and \
           data['verification_code'] == str(123):
            user.phone = data['phone']
            user.save()
            content = 'Your phone number has been modified!'
            sendmessage(self.request, content)
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
            user.verifycode = random.randrange(0, 999999)
            user.save()
            #print user.verifycode
            #content = 'verifycode:' + str(user.verifycode)
            #utils.send_msg(data['phone'], content)
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
            content = 'click here to active ' + \
                    '<a href="http://www.zufangbao.com/chargerent/">' \
                    'http://www.active.com</a>'
            utils.send_mail(data['email'], content)
            user.email = data['email']
            user.save()
            content = 'Your email has been modified!'
            sendmessage(self.request, content)
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
        if user and data['problem_one'] and \
           data['problem_two'] and data['problem_three']:
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


@require_auth
def messages(request):
    user = utils.get_user_obj(request)
    message = user.message_set.all()
    return utils.render('account/account_messages.html',
                        {'message': message})


@require_auth
def payments(request):
    pass

