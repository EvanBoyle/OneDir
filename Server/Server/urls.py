from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^OneDir/', 'DJServer.views.OneDir', name='OneDir'),
    url(r'^ListFiles/(?P<user>\w{0,50})/$', 'DJServer.views.ListFiles', name='ListFiles'),
    url(r'^GetFile/(?P<user>\w{0,50})/(?P<filename>.+)/$', 'DJServer.views.GetFile', name='GetFile'),
    #adjust path to reflect your directory to serve files from
    url(r'^Serve/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/hodor/OneDir/OneDir/Server/Files'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^LoggedIn/', 'DJServer.views.LoggedIn', name='LoggedIn'),
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token')

)


