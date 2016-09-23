from django.conf.urls import patterns, url
from fortune import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'KathySaadSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name = 'index'),
    url(r'^short/$', views.short, name = 'short'),
    url(r'^startrek/$', views.startrek, name = 'startrek'),
    url(r'^(?P<request_id>\d+)/$', views.detail, name = 'detail'),
)
