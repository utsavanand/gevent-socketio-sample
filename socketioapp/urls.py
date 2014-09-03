from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from socketio import sdjango
sdjango.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'socketioapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('echo_server.urls')),
    # url(r'^socket\.io', include(sdjango.urls)), 
    url("^socket\.io", include(sdjango.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
