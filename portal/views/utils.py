# -*- coding: utf-8 -*-
"""
Some helper function
"""

from django.shortcuts import render_to_response

from portal import models


def render(template_name, payment):
    return render_to_response('portal/%s' % template_name,
                              payment)


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
