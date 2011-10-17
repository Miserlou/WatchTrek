from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'watchtrek.views.home', name='home'),
    # url(r'^watchtrek/', include('watchtrek.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'tng/', 'watchtrek.tng.views.root'),
    url(r'tos/', 'watchtrek.tos.views.root'),
    url(r'^$', 'watchtrek.tng.views.root'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
