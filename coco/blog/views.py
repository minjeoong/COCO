from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt

def home(request, category_name=None):
    townblog = TownBlog.objects.filter(town=request.user.town).first()
    blog = Blog.objects.filter(townblog=townblog)

    if category_name:
        blog = blog.filter(category=category_name)

    paginator = Paginator(blog, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {'delivery_blogs': page_obj})

def detail(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    blog.is_liked = blog.likes.filter(user=request.user).exists()
    blog.like_count = blog.likes.count()
    return render(request,'detail.html', {'blog':blog})

def new(request):
    return render(request,'new.html')

def create(request):
    if request.method == 'POST':
        townblog = TownBlog.objects.get(town=request.user.town)
        new_blog = Blog()
        new_blog.townblog = townblog
        new_blog.user = request.user 
        new_blog.title = request.POST.get('title')
        new_blog.content = request.POST.get('content')
        new_blog.category = request.POST.get('category')
        new_blog.image = request.FILES.get('image')
        new_blog.save()
        return redirect('blog:detail', new_blog.id)
        
    return redirect('blog:home')

def edit(request, blog_id):
    edit_blog = Blog.objects.get(id=blog_id)

    return render(request, 'edit.html',{'edit_blog':edit_blog})

def update(request, blog_id):
    old_blog = get_object_or_404(Blog, pk=blog_id)
    old_blog.title = request.POST.get('title')
    old_blog.content = request.POST.get('content')
    old_blog.category = request.POST.get('category')
    old_blog.image = request.FILES.get('image')
    old_blog.save()
    return redirect('blog:home')

def delete(request, blog_id):
    delete_blog = get_object_or_404(Blog, pk=blog_id)
    delete_blog.delete()
    return redirect('blog:home')

def add_comment(request, blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        blog=get_object_or_404(Blog, pk=blog_id)
        comment_text = request.POST.get('comment_text')
        user = request.user
        comment = BlogComment(blog=blog, user=user, comment_text=comment_text)
        comment.save()
    return redirect('blog:detail', blog.id)

def update_comment(request, comment_id):
    print("dsfhjkashdfjklasdfkahdsfkjl")
    if request.method == 'POST':
        comment = get_object_or_404(BlogComment, pk=comment_id)
        comment.comment_text = request.POST.get('comment_text')
        comment.save()
    return redirect('blog:detail', comment.blog.id)

def delete_comment(request, comment_id):
    comment = get_object_or_404(BlogComment, pk=comment_id)
    blog_id = comment.blog.id
    comment.delete()
    return redirect('blog:detail', blog_id)

def like_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    user = request.user
    print(blog.likes)
    if blog.likes.filter(user=user).exists():
        liked = BlogLike.objects.get(blog=blog, user=user)
        liked.delete()
    else:
        liked = BlogLike(blog=blog, user=user)
        liked.save()

    return redirect('blog:detail', blog_id)
