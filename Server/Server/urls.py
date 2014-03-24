from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^OneDir/', 'DJServer.views.OneDir', name='OneDir'),
    url(r'^GetFiles/(?P<user>\w{0,50})/$', 'DJServer.views.GetFiles', name='GetFiles'),
    url(r'^admin/', include(admin.site.urls)),

)