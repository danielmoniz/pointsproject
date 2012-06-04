from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

from django.core.urlresolvers import reverse

class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/join.html'

    def dispatch(self, request, *args, **kwargs):
        # If the URL has a 'next' value, redirect appropriately.
        if request.GET['next']:
            self.success_url = request.GET['next']
        else:
            self.success_url = reverse('social:new_post')
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """Allow for auto-login and redirection."""
        user = form.save()
        user = authenticate(username=self.request.POST['username'], password=self.request.POST['password1'])
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)

