from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.models import User

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from social.models import Post, PostForm

class PostCreateView(CreateView):
    """The view for creating a post. Also handles listing posts on the global
    wall.
    """
    model = Post
    form_class = PostForm
    template_name = 'social/new_post.html'

    def dispatch(self, request, *args, **kwargs):
        """Ensure the correct success/failure URLs are set for redirection.
        """
        self.success_url = reverse('social:new_post')
        self.login_url = reverse('users:login') + '?next=' + request.path
        return super(PostCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """If the form is valid, check if the user is logged in. If not,
        redirect them to the login screen if they have tried to post.
        """
        post = form.save(commit=False)
        if self.request.user.is_authenticated():
            post.author = User.objects.get(id=self.request.user.id)
            post.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return HttpResponseRedirect(self.login_url)

    def get_context_data(self, **kwargs):
        """Add the list of posts to the page.
        If the user is not logged in, do not include the new_post form.
        """
        context = super(PostCreateView, self).get_context_data(**kwargs)

        # Add new_post form to the post list page.
        context['post_list'] = Post.objects.order_by('-date_created')

        if not self.request.user.is_authenticated():
            del context['form']
        return context

### DEPRECATED ###
class PostListView(ListView):
    """Provide a list of Post objects to a template."""
    queryset = Post.objects.order_by('-date_created')
    model = Post
    template_name = 'social/post_list.html'
    context_object_name = 'post_list'
