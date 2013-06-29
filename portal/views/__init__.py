from django.shortcuts import render_to_response


def render(template_name, payment):
    return render_to_response('portal/%s' % template_name,
                              payment)
