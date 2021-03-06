#encoding:utf-8
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response as RTR
from django.template import RequestContext as RC
from models import Account
from Product.models import ProductToSell, ProductToBuy
from django.contrib.auth import authenticate, login, logout
import datetime
#TODO user ajax authtication for register

def register(request):
    """
    register page and register handle
    """
    #TODO user authentication
    if request.method == 'GET':
        return RTR("register.html", {}, context_instance = RC(request))
    else:
        user_params = {
            'nickname' : request.POST.get('nickname', ''),
            'realname' : request.POST.get('real_name', ''),
            'password' : request.POST.get('password', ''),
            'dept' : request.POST.get('dept', ''),
            'intro' : request.POST.get('intro', ''),
            'address' : request.POST.get('address', ''),
            'email' : request.POST.get('email', ''),
            'qq' : request.POST.get('qq', ''),
            'phone' : request.POST.get('phone', '')}
        Account.create_user(user_params)
        return HttpResponse("register_ok.html!!!", {})

def logins(request):
    """
    login page and login handle
    """
    #TODO handle the request from the client
    if request.method == "GET":
        return RTR("login.html", {}, context_instance = RC(request))
    else:
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        user = authenticate(email = str(email), password = str(password))
        if user is not None:
            login(request, user)
            #TODO redirect to the personal page
            return HttpResponseRedirect('/user/%s' % user.nid) # return to the personal's page
        else:
            return HttpResponse("server error")

def logouts(request):
    logout(request)
    return HttpResponseRedirect('/')
    
def home(request, nid):
    """
    home page for user, user authentication needed
    """
    if not request.user.is_authenticated:                   # need login
        return HttpResponseRedirect('/register')
    else:
        user = Account.by_nid(nid)
        is_self = True if nid == request.user.nid else False
        cdic = {'user' : user,
                'is_self' : is_self}
        products = ProductToSell.latest_product_to_show()
        cdic['products'] = reversed(products)
        return RTR('user.html', cdic)

def home_release(request, nid):
    """
    home page for user, user authentication needed
    """
    if not request.user.is_authenticated:                   # need login
        return HttpResponseRedirect('/register')
    else:
        user = Account.by_nid(nid)
        is_self = True if nid == request.user.nid else False
        cdic = {'user' : user,
                'is_self' : is_self}
        products = ProductToSell.latest_product_to_show()
        cdic['products'] = reversed(products)
        return RTR('user.html', cdic)

def home_require(request, nid):
    """
    home page for user, user authentication needed
    """
    if not request.user.is_authenticated:                   # need login
        return HttpResponseRedirect('/register')
    else:
        user = Account.by_nid(nid)
        is_self = True if nid == request.user.nid else False
        cdic = {'user' : user,
                'is_self' : is_self}
        products = ProductToBuy.latest_product_to_show()
        cdic['products'] = reversed(products)
        return RTR('user.html', cdic)
        
        


def release(request):
    """
    release page and release handle
    """
    #TODO handle the request from the client
    
    if request.user.is_authenticated():
        if request.method == 'GET':
            return RTR("release.html", {}, context_instance = RequestContext(request))
        else:
            product_params = {
                'owner' : request.user,
                'productname' : request.POST.get('productname', ''),
                'broadtype' : request.POST.get('broadtype', ''),
                'image' : request.FILES.get('image'),
                'subtype' : request.POST.get('subtype', ''),
                'belongcampus' : request.POST.get('belongcampus', ''),
                'tradetype' : request.POST.get('tradetype', ''),
                'purity' : request.POST.get('purity', ''),
                'price' : request.POST.get('price', ''),
                'tradetitle' : request.POST.get('productname', ''),
                'tradedetail' : request.POST.get('tradedetail', ''),
                'releasetime' : datetime.datetime.now(),
                }
            print product_params
            ProductToSell.create_product_to_sell(product_params)
            return HttpResponse("add_product_to_sell.html!!!")    
    else:
        return RTR("login.html", {'error' : '璇峰厛鐧诲綍~'})
    
def require(request):
    """
    require page and handle
    """
    if request.user.is_authenticated():
        if request.method == 'GET':
            return RTR("require.html", {}, context_instance = RequestContext(request))
        else:
            product_params = {
                'owner' : request.user,
                'productname' : request.POST.get('productname', ''),
                'tradetype' : request.POST.get('tradetype', ''),
                'broadtype' : request.POST.get('broadtype', ''),
                'subtype' : request.POST.get('subtype', ''),
                'releasetime' : datetime.datetime.now(),
                }
            print product_params
            ProductToBuy.create_product_to_buy(product_params)
            return HttpResponse("add_product_to_buy.html!!!")    

    else:
        return RTR("login.html", {'error' : '璇峰厛鐧诲綍~'})
    
def news(request):
    """
    news page and handle
    """
    if request.user.is_authenticated():
        return RTR("news.html", {})
    else:
        return RTR("login.html", {'error' : '请先登录~'})
    
def search(request):
    """
    search page and handle
    """
    return RTR('search.html', {})


