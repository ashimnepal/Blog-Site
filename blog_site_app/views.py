from django.shortcuts import render
from blog_site_app.models import BlogPost
from django.http import HttpResponseRedirect
from .forms import PostForm

# Create your views here.

def post_list(request):
    posts = BlogPost.objects.all()
    return render (request,"post_list.html", {"all_posts": posts},)

def post_detail(request,pk):
    post = BlogPost.objects.get(pk=pk)
    return render(request, "post_details.html", {"detailed_post": post},)
    
def post_add(request):    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()        
        return HttpResponseRedirect("/")
    else:
        form = PostForm()
        return render(request, "post_add.html", {'form': form})