#coding=utf-8
from django.shortcuts import render,get_object_or_404
from .models import Post,Category
import markdown
from comments.forms import CommentForm
from django.views.generic import ListView
# Create your views here.

# class IndexView(ListView):
#     model = Post
#     template_name = 'blog/index.html'
#     post_list = Post.objects.all()
#     context_object_name = post_list

def index(request):
    # return HttpResponse("欢迎访问我的官网首页")
    post_list = Post.objects.all()
    for post in post_list:
        post.excerpt = markdown.markdown(post.excerpt,
                                      extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                      ])
    return render(request,'blog/index.html',{"post_list":post_list})

def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.increase_views()
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    comment_list = post.comment_set.all()
    content = {"post":post,"form":CommentForm(),"comment_list":comment_list}
    return render(request,'blog/detail.html',content)

def archives(request,year,month):
    post_list = Post.objects.filter(created_time__year=year,created_time__month=month).order_by("-created_time")
    return render(request,"blog/index.html",{"post_list":post_list})

def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request,"blog/index.html",{"post_list":post_list})

