#encoding:utf-8
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response as RTR
from django.template import RequestContext as RC
from User.models import Account
from django.contrib.auth import authenticate, login, logout

def manage(request):
    """
    manage page
    """
    #TODO judge whether the user is the super user
    return RTR('manage.html', {})

def manage_buy(request):
    """
    manage page
    """
    #TODO judge whether the user is the super user
    return RTR('manage_buy.html', {})
