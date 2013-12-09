from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import settings
from Index.views import home, rules, contact, market
from User.views import release, login, register
from Product.views import product_detail
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SHM.views.home', name='home'),
    # url(r'^SHM/', include('SHM.foo.urls')),
    url(r'^$', home),
    url(r'^rules$', rules),
    url(r'^contact$', contact),
    url(r'^market$', market),
    url(r'^product/(?P<pid>\d+)$', product_detail),
    url(r'^release$', release),
    url(r'^login$', login),
    url(r'^register$', register),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.STATIC_ROOT}),
    
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
