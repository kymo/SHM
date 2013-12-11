# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response as RTR
from models import ProductToSell

def product_detail(request, pid):
    """
    get the product information from pid
    """
    #TODO show the detail of product
    is_self = request.user.is_authenticated()
    cdic = {}
    product = ProductToSell.objects.get(id = int(pid))
    # TODO get the same products
    same_products = ProductToSell.objects.filter(broad_type = product.broad_type)[:5]
    cdic['is_self'] = is_self
    cdic['same_products'] = same_products
    cdic['product'] = product
    
    
    return RTR('product_details.html', cdic)
