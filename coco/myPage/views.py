from django.shortcuts import render,redirect, get_object_or_404
from .models import Mypage, MypageArticle, Liked, Comment
from user.models import Profile, CustomUser
from django.http import JsonResponse
from django.db.models import Count
import os

def myPage(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    myPage = get_object_or_404(Mypage, user=user)
    if request.user.town == user.town:
        articles = MypageArticle.objects.filter(mypage__user=user)
        profile = user.profile
        return render(request, 'myPage.html', {'articles': articles, 'profile': profile, 'owner':user, 'myPage':myPage})
    return redirect('town:mainPage')

def newArticle(request):
    return render(request,'newArticle.html')

def createArticle(request):
    if request.method == 'POST':
        mypage = Mypage.objects.get(user=request.user)
        article = MypageArticle(mypage = mypage)
        article.title = request.POST.get('title')
        article.content_text = request.POST.get('content')
        if request.FILES.get('image'):
            article.image = request.FILES.get('image')        
        article.save()
        return redirect('myPage:detailArticle', article.id)
    else:
        return render(request, 'newArticle.html')
    
def detailArticle(request, article_id):
    article = get_object_or_404(MypageArticle, id=article_id)
    article.is_liked = article.likes.filter(user=request.user).exists()
    article.article_like = article.likes.count()
    return render(request, 'detailArticle.html', {'article': article})

def editArticle(request, article_id):
    edit_article = MypageArticle.objects.get(id=article_id)
    return render(request, 'editArticle.html',{'edit_article':edit_article})

def updateArticle(request, article_id):
    old_article = get_object_or_404(MypageArticle, pk=article_id)
    old_article.title = request.POST.get('title')
    old_article.content_text = request.POST.get('content')
    if request.FILES.get('image'):
        if old_article.image:
            delete_image(old_article.image.path)
        old_article.image = request.FILES.get('image')
    old_article.save()
    return redirect('myPage:detailArticle', old_article.id)

def deleteArticle(request, article_id):
    article = get_object_or_404(MypageArticle, id=article_id)
    
    # 현재 로그인한 사용자와 게시물의 소유자가 같을 때만 삭제 가능하도록 체크
    if request.user == article.mypage.user:
        if article.image:
            delete_image(article.image.path)
        article.delete()
    
    return redirect('myPage:myPage', user_id=request.user.id)
    
def like_article(request, article_id):
    article = get_object_or_404(MypageArticle, id=article_id)
    user = request.user

    if article.likes.filter(user=user).exists():
        liked = Liked.objects.get(article=article, user=user)
        liked.delete()
    else:
        liked = Liked(article=article, user=user)
        liked.save()

    return redirect('myPage:detailArticle', article.id)


def create_comment(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(MypageArticle, id=article_id)
        text = request.POST.get('comment_text')
        user = request.user
        comment = Comment(article=article, user=user, text=text)
        comment.save()
        return redirect('myPage:detailArticle', article.id)
    return render(request, 'myPage.html')

def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, id = comment_id)
    comment.text = request.POST.get('comment')
    comment.save()
    return redirect('myPage:detailArticle', comment.article.id)

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    id = comment.article.id
    # 현재 로그인한 사용자와 댓글의 작성자가 같을 때만 삭제 가능하도록 체크
    if request.user == comment.user:
        comment.delete()
    return redirect('myPage:detailArticle', id)


def upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        myPage = get_object_or_404(Mypage, user=request.user)
        file = request.FILES['file']
        title = request.POST.get('title')
        if title == 'mainImage':
            if myPage.mainImage:
                path = myPage.mainImage.path
                delete_image(path)
            myPage.mainImage = file
        elif title == 'subImage1':
            if myPage.subImage1:
                path = myPage.subImage1.path
                delete_image(path)
            myPage.subImage1 = file
        elif title == 'subImage2':
            if myPage.subImage2:
                path = myPage.subImage2.path
                delete_image(path)
            myPage.subImage2 = file
        elif title == 'subImage3':
            if myPage.subImage3:
                path = myPage.subImage3.path
                delete_image(path)
            myPage.subImage3 = file
        myPage.save()
        
        return JsonResponse({'message': '파일 업로드 성공'})
    
    # 파일 업로드 실패 응답 반환
    return JsonResponse({'message': '파일 업로드 실패'}, status=400)

def deleteImage(request):
    imageId = request.POST.get('imageId')
    print(imageId)
    myPage = get_object_or_404(Mypage, user=request.user)
    if imageId == 'mainImage':
        path = myPage.mainImage.path
        delete_image(path)
        myPage.mainImage.delete()
    elif imageId == 'subImage1':
        path = myPage.subImage1.path
        delete_image(path)
        myPage.subImage1.delete()
    elif imageId == 'subImage2':
        path = myPage.subImage2.path
        delete_image(path)
        myPage.subImage2.delete()
    elif imageId == 'subImage3':
        path = myPage.subImage3.path
        delete_image(path)
        myPage.subImage3.delete()
    myPage.save()
    return redirect('myPage:myPage', request.user.id)

def delete_image(path):
    # 이미지 파일 삭제
    print(path,'삭제')
    if os.path.exists(path):
        os.remove(path)
