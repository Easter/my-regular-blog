from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from blog import urls
from .models import Comment
from.forms import CommentForm
# Create your views here.

def post_comment(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect(post)

        else:
            comment_list = post.comment_set.all()
            post = post
            form = form
            return render(request,"blog/detail.html",{"post":post,"form":form,"comment_list":comment_list})
    return redirect(post)