# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response as RTR

def index(request):
    """
    home page for user request
    """
    return RTR('index.html', {})

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
    return RTR('market.html', {})
    
