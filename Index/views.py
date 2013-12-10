# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response as RTR

def index(request):
    """
    home page for user request
    """
    #TODO load news
    #TODO load newest release
    #TODO load newest deal
    #TODO load newest require
    cdic = {}
    if request.user.is_authenticated():
        cdic['is_self'] = True
        print 'yes'
        cdic['user'] = request.user
    else:
        cdic['is_self'] = False
    return RTR('index.html', cdic, context_instance = RequestContext(request))

def rules(request):
    """
    rules page
    """
    #TODO user anthentication
    return RTR('rules.html', {})

def contact(request):
    """
    contact page
    """
    #TODO user authentication
    return RTR('contact.html', {})

def market(request):
    """
    market page
    """
    #TODO user authentication
    #TODO get the products from db
    t = request.GET.get('t', '')
    if t == '':
        t = 'b'
    cdic = {'t' : t}
    if request.user.is_authenticated():
        cdic['is_self'] = True
        cdic['user'] = request.user
    else:
        cdic['is_self'] = False
    return RTR('market.html', cdic)
    
