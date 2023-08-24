from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import BlogPost , Comment


# @login_required
@csrf_exempt
def create_blog_post(request):
    if request.method == "POST":
        title= request.POST.get('title')
        content = request.POST.get("content")
        author = request.user
        blog_post = BlogPost.objects.create(title=title,content=content,author=author)
        Comment.objects.create(content=content, author=author, blog_post=blog_post)
        return JsonResponse({'message': 'Comment created successfully'})
    return render(request,'blog/home.html')
@login_required
@csrf_exempt

def create_comments(request,blog_post_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        author = request.user
        blog_post = BlogPost.objects.get(pk = blog_post_id)
        Comment.objects.create(content = content, author=author,blog_post=blog_post)
        return JsonResponse({'message': 'Comment created successfully'})
def list_blog_posts(request):
    blog_post = BlogPost.objects.all()
    data =[{'title':post.title, 'content':post.content} for post in blog_post]
    return JsonResponse(data,safe=False)
    
    
def list_comments(request,blog_post_id):
    comments = Comment.objects.filter(blog_post_id=blog_post_id)
    data = [{'content':comment.content}for comment in comments]
    return JsonResponse(data,safe = False)

@login_required
@csrf_exempt
def update_blog_post(request, blog_post_id):
    try:
        blog_post = BlogPost.objects.get(pk = blog_post_id)
        if request.user != blog_post.author:
            return JsonResponse({'error':"you are not authorized to update this post"},status=403)
        
        
        if request.method == 'POST':
            title = request.POST.get('title')
            content = request.POST.get('content')
            blog_post.title = title
            blog_post.content = content
            blog_post.save()
            return JsonResponse({'message': 'Blog post updated successfully'})
    except BlogPost.DoesNotExist:
        return JsonResponse({'error': 'Blog post not found'}, status=404)