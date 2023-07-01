from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

app_name = 'myPage'
urlpatterns = [
    path('<int:user_id>', myPage, name='myPage'),
    path('newArticle/', newArticle, name='newArticle'),
    path('createArticle/', createArticle, name='createArticle'),
    path('detailArticle/<int:article_id>/', detailArticle, name='detailArticle'),
    path('deleteArticle/<int:article_id>/', deleteArticle, name='deleteArticle'),
    path('like/<int:article_id>/', like_article, name='like_article'),
    path('article/<int:article_id>/comment/create/',create_comment, name='create_comment'),
    path('article/<int:article_id>/comment/delete/',create_comment, name='delete_comment'),
]
