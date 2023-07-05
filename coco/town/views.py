from django.shortcuts import render
from .models import Town
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import TownBlog, Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

def townList(request):
    if request.user.town:
        return redirect('town:mainPage')

    search_query = request.GET.get('search_field', '')
    townlist = Town.objects.all()

    if search_query:
        townlist = townlist.filter(townname__icontains=search_query)

    return render(request, 'townList.html', {'townlist': townlist, 'search_query': search_query})


def newTown(request):
    if request.user.town:
        return redirect('town:mainPage')
    return render(request, 'newTown.html')

def createTown(request):
    if request.method == 'POST':
        new_town = Town()
        new_town.townname = request.POST.get('townname')
        new_town.save()
        townblog = TownBlog.objects.create(town = new_town)
        
    return redirect('town:townList')

def setTown(request, town_id):
    town = get_object_or_404(Town, pk = town_id)
    user = request.user
    user.town = town
    user.save()
    user.town.usercount = town.users.count()
    
    town.save()
    return redirect('town:mainPage')

def mainPage(request):
    if request.user.town is None:
        return redirect('town:townList')
    town = request.user.town
    townblog = get_object_or_404(TownBlog, town = town)
    blogs = Blog.objects.filter(townblog=townblog)
    
    latest_blog = blogs.order_by('-created_at').first()
    most_viewed_blog = blogs.order_by('-hit').first()
    most_liked_blog = blogs.order_by('-likes').first()

    return render(request, 'mainPage.html', {
        'town': town,
        'latest_blog': latest_blog,
        'most_viewed_blog': most_viewed_blog,
        'most_liked_blog': most_liked_blog
    })

def myTown(request):
    town = request.user.town
    users = town.users.all()
    return render(request, 'myTown.html', {'users':users})
    
def setting(request):
    return render(request, 'setting.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('currentPassword')
        new_password = request.POST.get('newPassword')
        confirm_password = request.POST.get('confirmPassword')

        # 현재 비밀번호 확인
        if not request.user.check_password(current_password):
            messages.error(request, '현재 비밀번호가 일치하지 않습니다.')
            return redirect('town:setting')

        # 새로운 비밀번호와 비밀번호 확인 일치 여부 확인
        if new_password != confirm_password:
            messages.error(request, '새로운 비밀번호와 비밀번호 확인이 일치하지 않습니다.')
            return redirect('town:setting')

        # 비밀번호 변경
        request.user.set_password(new_password)
        request.user.save()

        # 세션 업데이트
        update_session_auth_hash(request, request.user)

        messages.success(request, '비밀번호가 성공적으로 변경되었습니다.')
        return redirect('town:mainPage')

    return redirect('town:setting')
