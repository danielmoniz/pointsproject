from django.conf.urls import patterns, include, url

urlpatterns = patterns('social.views', 
    url(r'^$', 'home', name='home'),
)
