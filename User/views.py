# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response as RTR


def register(request):
    """
    register page and register handle
    """
    #TODO handle the request from client
    return RTR("register.html", {})


def login(request):
    """
    login page and login handle
    """
    #TODO handle the request from the client
    return RTR("login.html", {})


def release(request):
    """
    release page and release handle
    """
    #TODO handle the request from the client
    return RTR("release.html", {})

