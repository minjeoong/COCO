from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog, Comment, Tag, Like
from django.core.paginator import Paginator
from .forms import BlogForm
from .forms import CommentForm

def home(request):
    tagged_blogs = Blog.objects.filter(tag__name='배달')
    paginator = Paginator(tagged_blogs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'home.html',{'delivery_blogs':page_obj})

def detail(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    tags = blog.tag.all()
    likes = len(Like.objects.filter(blog=blog))
    return render(request,'detail.html', {'blog':blog, 'tags':tags, 'likes':likes})

def new(request):
    tags = Tag.objects.all()
    return render(request,'new.html', {'tags':tags})

def create(request):
   form = BlogForm(request.POST)
   if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.save()
        tags = request.POST.getlist('tags')
        for tag_id in tags:
            tag = Tag.objects.get(id=tag_id)
            new_blog.tag.add(tag)
        return redirect('blog:detail', new_blog.id)
   return redirect('blog:home')

def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html',{'edit_blog':edit_blog})

def update(request, blog_id):
    old_blog = get_object_or_404(Blog, pk=blog_id)
    form = BlogForm(request.POST, instance=old_blog)
    if form.is_valid():
       new_blog = form.save(commit=False)
       new_blog.save()
       return redirect('blog:detail', old_blog.id)
    return redirect('blog:home')

def delete(request, blog_id):
    delete_blog = get_object_or_404(Blog, pk=blog_id)
    delete_blog.delete()
    return redirect('home')

def add_comment_to_post(request, blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)
    if request.method == "GET":
        form=CommentForm(request.GET)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=blog
            comment.save()
            return redirect('blog:detail', blog.id)
        else:
            form=CommentForm()
        return render(request, 'add_comment_to_post.html', {'form':form})
    
def like(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    like = Like(blog=blog)
    like.save()
    return redirect('blog:detail', blog_id)

def product(request):
    tagged_blogs = Blog.objects.filter(tag__name='생필품')
    paginator = Paginator(tagged_blogs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'product.html',{'product_blogs':page_obj})

def ingredient(request):
    tagged_blogs = Blog.objects.filter(tag__name='식재료')
    paginator = Paginator(tagged_blogs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'ingredient.html',{'ingredient_blogs':page_obj})

def etc(request):
    tagged_blogs = Blog.objects.filter(tag__name='기타')
    paginator = Paginator(tagged_blogs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'etc.html',{'etc_blogs':page_obj})