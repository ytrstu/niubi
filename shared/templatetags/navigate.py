# -*- coding: utf8 -*-
from django.template import Library
from lib.http.auth import is_admin
from google.appengine.api import users
from django.utils.safestring import mark_safe

register = Library()

@register.inclusion_tag('navigator.html', takes_context=True)
def navigator(context):
    context['is_admin'] = is_admin()  
    return context