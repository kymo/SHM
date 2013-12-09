#encoding:utf-8
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response as RTR
from django.template import RequestContext as RC
from models import Account
from django.contrib.auth import authenticate, login
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
        return HttpResponse("register_ok.html", {})

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
        print user.id
        if user is not None:
            login(request, user)
            #TODO redirect to the personal page
            return HttpResponseRedirect('/user/%s' % user.nid) # return to the personal's page
        else:
            return HttpResponse("server error")


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
        return RTR('user.html', cdic)
        
        


def release(request):
    """
    release page and release handle
    """
    #TODO handle the request from the client
    if request.user.is_authenticated():
        
        return RTR("release.html", {})
    else:
        return RTR("login.html", {'error' : 'ÇëÏÈµÇÂ¼~'})
    
def require(request):
    """
    require page and handle
    """
    if request.user.is_authenticated():
        return RTR("require.html", {})
    else:
        return RTR("login.html", {'error' : 'ÇëÏÈµÇÂ¼~'})
    
def news(request):
    """
    news page and handle
    """
    if request.user.is_authenticated():
        return RTR("news.html", {})
    else:
        return RTR("login.html", {'error' : 'ÇëÏÈµÇÂ¼~'})
