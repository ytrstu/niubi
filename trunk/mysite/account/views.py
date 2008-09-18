# -*- coding: utf-8 -*-
import logging

from django.http import HttpResponseRedirect, Http404
from django.http import HttpResponse
from django.template.context import RequestContext
from django.shortcuts import render_to_response

from google.appengine.ext import db
from google.appengine.api import users

from mysite.utils.webutils import login_required, admin_required, is_admin, object_list

from models import UserSettings
from forms import UserSettingsForm

def login(request):
    if request.GET.has_key('next'):
        next = request.GET['next']
    else:
        next = '/'
    return HttpResponseRedirect(users.create_login_url(next))

def logout(request):
    return HttpResponseRedirect(users.create_logout_url('/'));

@login_required
def setting(request):
    settings = UserSettings.getByCurrentUser()
    im_protocol = '' # settings.im.protocol
    im_address = '' # settings.im.address    
    if request.method == 'GET':
        form = UserSettingsForm({'firstname':settings.firstname,
                                 'lastname':settings.lastname,
                                 'gender':settings.gender,
                                 'profile': settings.profile,
                                 'language': settings.language})
    if request.method == 'POST':
        form = UserSettingsForm(request.POST)
        logging.getLogger().debug(form)
        if form.is_valid():
            modified_settings = form.save(commit=False)
            settings.firstname = modified_settings.firstname
            settings.lastname = modified_settings.lastname                    
            settings.gender = modified_settings.gender
            settings.profile = modified_settings.profile
            settings.language = modified_settings.language
            settings.birthdate = modified_settings.birthdate
            settings.website = modified_settings.website
            settings.home_phone = modified_settings.home_phone
            settings.work_phone = modified_settings.work_phone
            settings.mobile = modified_settings.mobile
            settings.fax = modified_settings.fax
            settings.address = modified_settings.address
            if request.POST['im_address'] is not u'':
                settings.im = db.IM(request.POST['im_protocol'], request.POST['im_address'])
            settings.put()
            return HttpResponseRedirect('/')
    return render_to_response('account/setting.html', {'im_protocol':im_address,'im_protocol':im_address,'form': form}, context_instance=RequestContext(request))