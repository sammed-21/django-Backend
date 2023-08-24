from django.urls import path
from .views import create_blog_post,create_comments,list_blog_posts,list_comments,update_blog_post

urlpatterns = [
    path('',create_blog_post),
    path('create-blog/',create_blog_post,name="create-post"),
    path('create-comment/<int:blog_post_id>/',create_comments,name='create-comment'),
    path('list-post',list_blog_posts,name='list-posts'),
    path('list-comments/<int:blog_post_id>/',list_comments,name='list-comments'),
    path('update-post/<int:blog_post_id>',update_blog_post,name='update-post'),
    
]
