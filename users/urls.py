from django.conf.urls import patterns, include, url

from users.views import UserCreateView

urlpatterns = patterns('', 
    url(r'^join/$', UserCreateView.as_view(), name='join'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
)
