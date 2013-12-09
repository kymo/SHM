# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response as RTR

def product_detail(request, pid):
    """
    get the product information from pid
    """
    #TODO show the detail of product
    
    return RTR('product_details.html', {})
