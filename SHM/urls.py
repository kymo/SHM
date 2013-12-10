from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import settings
from Index.views import index, rules, contact, market
from User.views import release, logins, register, home, require, news, logouts, search
from Product.views import product_detail
from Manage.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SHM.views.home', name='home'),
    # url(r'^SHM/', include('SHM.foo.urls')),
    url(r'^$', index),
    url(r'^rules$', rules),
    url(r'^contact$', contact),
    url(r'^market$', market),
    url(r'^release$', release),
    url(r'^require$', require),
    url(r'^news$', news),
    
    url(r'^logout$', logouts),
    url(r'^login$', logins),
    url(r'^register$', register),
    url(r'^search$', search),
    
    #manage page
    url(r'^manage$', manage),
    url(r'^manage/product_to_buy$', manage_buy),
    #user personal page
    url(r'^user/(?P<nid>\d+)$', home),
    #product page
    url(r'^product/(?P<pid>\d+)$', product_detail),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.STATIC_ROOT}),
    
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
