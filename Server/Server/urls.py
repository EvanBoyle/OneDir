from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^OneDir/', 'DJServer.views.OneDir', name='OneDir'),
    url(r'^ListFiles/(?P<user>\w{0,50})/$', 'DJServer.views.ListFiles', name='ListFiles'),
    url(r'^UploadFile/$', 'DJServer.views.UploadFile', name='UploadFile'),
    url(r'^GetFile/(?P<user>\w{0,50})/(?P<filename>.+)/$', 'DJServer.views.GetFile', name='GetFile'),
    url(r'^DeleteFile/(?P<user>\w{0,50})/(?P<filename>.+)/$', 'DJServer.views.DeleteFile', name='DeleteFile'),
    url(r'^DeleteUser/(?P<user>\w{0,50})/$', 'DJServer.views.DeleteUser', name='DeleteUser'),
    #adjust path to reflect your directory to serve files from
    url(r'^Serve/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '../Files'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^LoggedIn/', 'DJServer.views.LoggedIn', name='LoggedIn'),
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^CreateUser/', 'DJServer.views.CreateUser', name='CreateUser'),
    url(r'^ChangePassword/', 'DJServer.views.ChangePassword', name='ChangePassword'),

)
