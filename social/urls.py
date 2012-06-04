from django.conf.urls import patterns, include, url

from social.views import PostCreateView, PostListView

urlpatterns = patterns('social.views', 
    #url(r'^$', 'home', name='home'),
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^new_post/$', PostCreateView.as_view(), name='new_post'),
)
