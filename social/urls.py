from django.conf.urls import patterns, include, url

from social.views import PostCreateView, PostListView

urlpatterns = patterns('social.views', 
    url(r'^$', PostCreateView.as_view(), name='new_post'),
)
