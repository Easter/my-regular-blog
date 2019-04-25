from django import template
from ..models import Post,Category
register = template.Library()

@register.simple_tag # 最新文章模板标签
def get_recent_blog(num=5):
    return Post.objects.all().order_by("-created_time")[:num]

@register.simple_tag # 最近归档模板标签
def archives():
    return Post.objects.dates('created_time','month',order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.all()

@register.simple_tag
def get_blog_numbers():
    # categories = Category.objects.all()
    # for category in categories:
    #     post_list = Post.objects.filter(category=category.name)
    #     return post_list
    return Post.objects.all()





