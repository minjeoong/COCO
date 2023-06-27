from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog, Comment, Tag
from .forms import BlogForm
from .forms import CommentForm

def home(request):
    blogs = Blog.objects.all()
    return render(request,'home.html',{'blogs':blogs})

def detail(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    tags = blog.tag.all()
    return render(request,'detail.html', {'blog':blog, 'tags':tags})

def new(request):
    tags = Tag.objects.all()
    return render(request,'new.html', {'tags':tags})
    
def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.content = request.POST['content']
    new_blog.save()
    tags = request.POST.getlist('tags')
    for tag_id in tags:
        tag = Tag.objects.get(id=tag_id)
        new_blog.tag.add(tag)
    return redirect('blog:detail', new_blog.id)

#def create(request):
#    form = BlogForm(request.POST)

   # 착한 사용자
#    if form.is_vaild():
#        new_blog = form.save(commit=False)
#        new_blog.save()
#        return redirect('detail', new_blog.id)
    
    # 나쁜 사용자
#    return render(request, "new.html")

def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html',{'edit_blog':edit_blog})

def update(request, blog_id):
    old_blog = get_object_or_404(Blog, pk=blog_id)
    old_blog.title = request.POST['title']
    old_blog.content = request.POST['content']
    old_blog.save()
    return redirect('detail', old_blog.id)

# def update(request, blod_id):
#    old_blog = get_object_or_404(Blog, pk=blog_id)
#    form = BlogForm(request.POST, instance=old_blog)

    # 착한 사용자
    #if form.is_valid():
    #    new_blog = form.save(commit=False)
    #    new_blog.save()
    #    return redirect('detail', old_blog.id)
    
    # 나쁜 사용자
    #return redirect(request, "new.html")

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