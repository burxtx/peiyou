from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^peiyou/training/', include('training.urls', namespace='training')),
    url(r'^peiyou/admin/', include(admin.site.urls)),
)
