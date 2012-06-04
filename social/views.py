from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.views.generic import CreateView, ListView, DetailView
#from django.template import RequestContext

from social.models import Post, PostForm

def home(request):
    #return HttpResponse('test')
    return render_to_response('social/home.html')

class PostListView(ListView):
    queryset = Post.objects.order_by('-date_created')
    model = Post
    template_name = 'social/post_list.html'
    context_object_name = 'post_list'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'social/new_post.html'
    success_url = '/test'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return HttpResponseRedirect(self.success_url)

