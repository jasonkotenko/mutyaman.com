from django import template
from posts.models import Post

register = template.Library()

@register.inclusion_tag('posts/_recent.html')
def latest_posts():
  posts = Post.objects.all().order_by('-pub_date')[:5]
  return {'posts': posts}

