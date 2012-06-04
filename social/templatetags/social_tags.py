from django import template
from social.models import Post
from social.views import PostCreateView

register = template.Library()

class NewPostNode(template.Node):
    def render(self, context):
        post_create_view = PostCreateView.as_view()
        return post_create_view(context)

def new_post_form(parser, token):
    try:
        tag_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, 'bad tag'
    return NewPostNode()

register.tag('new_post_form', new_post_form)
