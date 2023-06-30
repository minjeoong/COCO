from django.shortcuts import render,redirect, get_object_or_404
from .models import Mypage, MypageArticle, Liked, Comment
from user.models import Profile, CustomUser

from django.db.models import Count


def myPage(request, user_id):
    
    user = get_object_or_404(CustomUser, pk=user_id)
    if request.user.town == user.town:
        articles = MypageArticle.objects.filter(mypage__user=user).annotate(like_count=Count('likes'))
        profile = user.profile
        for article in articles:
            article.is_liked = article.likes.filter(user=request.user).exists()

        return render(request, 'myPage.html', {'articles': articles, 'profile': profile, 'owner':user})
    return redirect('town:mainPage')


def newArticle(request):
    return render(request,'newArticle.html')

def createArticle(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        mypage = Mypage.objects.get(user=request.user)
        article = MypageArticle(mypage=mypage, content_text=content)
        article.save()
        category = request.POST.get('category')
        print(category)
        return redirect('myPage:myPage', request.user.id)
    else:
        return render(request, 'newArticle.html')
    
def deleteArticle(request, article_id):
    article = get_object_or_404(MypageArticle, id=article_id)
    
    # 현재 로그인한 사용자와 게시물의 소유자가 같을 때만 삭제 가능하도록 체크
    if request.user == article.mypage.user:
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

    return redirect('myPage:myPage', user_id=article.mypage.user_id)


def create_comment(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(MypageArticle, id=article_id)
        text = request.POST.get('comment_text')

        user = request.user

        comment = Comment(article=article, user=user, text=text)
        comment.save()

        return redirect('myPage:myPage', user_id=article.mypage.user_id)

    return render(request, 'myPage.html')

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # 현재 로그인한 사용자와 댓글의 작성자가 같을 때만 삭제 가능하도록 체크
    if request.user == comment.user:
        comment.delete()

    return redirect('myPage:myPage', user_id=comment.article.mypage.user_id)

