"""
URL configuration for BlogSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog_site_app import views

urlpatterns = [
    path("", views.post_list),
    path("post-detail/<int:pk>/", views.post_detail),
    path("draft-detail/<int:pk>/", views.draft_detail),
    path("blog_add/", views.post_add),
    path("drafts-list/", views.post_draft),
    path("post-delete/<int:pk>/", views.post_delete),
    path("post-edit/<int:pk>/", views.post_edit),
    
]
