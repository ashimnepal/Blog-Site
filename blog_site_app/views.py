from django.shortcuts import render, get_object_or_404,redirect
from blog_site_app.models import BlogPost
from django.http import HttpResponseRedirect
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.

def post_list(request):
    posts = BlogPost.objects.filter(published_date__lte = timezone.now()).order_by("-published_date")
    return render (request,"post_list.html", {"all_posts": posts},)

def post_detail(request,pk):
    # post = BlogPost.objects.get(pk=pk)
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, "post_details.html", {"detailed_post": post},)
@login_required    
def post_add(request):    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()       
        return HttpResponseRedirect("/")
    else:
        form = PostForm()
        return render(request, "post_add.html", {'form': form})
@login_required   
def post_draft(request):
    drafts = BlogPost.objects.filter(published_date__isnull=True).order_by("-date")
    return render(request, "draft_list.html", {"drafts_list" : drafts})
@login_required
def draft_detail(request,pk):
    # post = BlogPost.objects.get(pk=pk)
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, "draft_detail.html", {"draft_detailed": post},)
@login_required
def post_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    post.delete()
    return HttpResponseRedirect("/")
    
# def post_edit(request, pk):    
#     post = get_object_or_404(BlogPost, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return HttpResponseRedirect("/")
#     else:
#         form = PostForm(instance=post)
#     return render(request, "post_edit.html", {"form": form, "post":post},)

@login_required
def post_edit(request, pk):    
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect("/")
    else:
        form = PostForm(instance=post)
    return render(request, "post_add.html", {"form": form},)