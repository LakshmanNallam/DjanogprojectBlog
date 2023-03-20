from datetime import date
from django.shortcuts import render,get_object_or_404
from .models import Post

post=[]

def get_date(eacItem):
    return eacItem["date"]

def home(request):
    post=Post.objects.all().order_by("data")
    latest_posts=post[:3]
    return render(request,"blog/home.html",{"posts":latest_posts})

def postDetails(request,slug):
    #obj=Post.objects.get(slug=slug)
    obj=get_object_or_404(Post,slug=slug)
    return render(request,"blog/postDetails.html",{"obj":obj,"allTagsList":obj.tag.all()})

def posts(request):
    post=Post.objects.all().order_by("data")
    return render(request,"blog/posts.html",{"posts":post})