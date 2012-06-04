from django.db import models
from django import forms
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{}: {}'.format(self.author.username, self.body)

#### FORMS ####

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)
