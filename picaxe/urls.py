from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.sites.models import Site

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'picaxe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
)

admin.site.unregister(Site)
