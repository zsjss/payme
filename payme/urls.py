from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('portal.urls')),
    url(r'^z/', include('portal.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
