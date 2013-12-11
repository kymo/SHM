# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response as RTR
from Product.models import ProductToSell

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
    t = request.GET.get('t', 'a')
    p = request.GET.get('p', '1')
    cdic = {'t' : t}
    if request.user.is_authenticated():
        cdic['is_self'] = True
        cdic['user'] = request.user
        
    else:
        cdic['is_self'] = False
    products, page = ProductToSell.by_type(t, int(p))
    cdic['products'] = products
    cdic['bef_page'] = page - 1 if page > 0 else 1
    cdic['t'] = t
    cdic['page'] = page
    cdic['nxt_page'] = page + 1
    return RTR('market.html', cdic, context_instance = RequestContext(request))
    
