from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    pass

class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'users/join.html'
