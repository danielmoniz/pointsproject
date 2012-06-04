from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.views.generic import CreateView, ListView, DetailView
#from django.template import RequestContext

from social.models import Post, PostForm

class PostCreateView(CreateView):
    """The view for creating a post. Also handles listing posts."""
    model = Post
    form_class = PostForm
    template_name = 'social/new_post.html'

    def dispatch(self, request, *args, **kwargs):
        self.success_url = reverse('social:new_post')
        return super(PostCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)

        # Add new_post form to the post list page.
        context['post_list'] = Post.objects.order_by('-date_created')

        return context

### DEPRECATED ###
class PostListView(ListView):
    queryset = Post.objects.order_by('-date_created')
    model = Post
    template_name = 'social/post_list.html'
    context_object_name = 'post_list'
