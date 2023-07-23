from django.shortcuts import render
from blog_site_app.models import BlogPost

# Create your views here.

def post_list(request):
    posts = BlogPost.objects.all()
    return render (request,"post_list.html", {"all_posts": posts},)

def post_detail(request,pk):
    post = BlogPost.objects.get(pk=pk)
    return render("post_detail.html", {"detailed_post": post},)
