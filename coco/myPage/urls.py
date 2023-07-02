from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

app_name = 'myPage'
urlpatterns = [
    path('<int:user_id>/', myPage, name='myPage'),
    path('upload/', upload, name='upload'),
    path('newArticle/', newArticle, name='newArticle'),
    path('createArticle/', createArticle, name='createArticle'),
    path('detailArticle/<int:article_id>/', detailArticle, name='detailArticle'),
    path('editArticle/<int:article_id>/', editArticle, name='editArticle'),
    path('updateArticle/<int:article_id>/', updateArticle, name='updateArticle'),
    path('deleteArticle/<int:article_id>/', deleteArticle, name='deleteArticle'),
    path('like/<int:article_id>/', like_article, name='like_article'),
    path('create_comment/<int:article_id>/',create_comment, name='create_comment'),
    path('update_comment/<int:comment_id>/',update_comment, name='update_comment'),
    path('delete_comment/<int:comment_id>/',delete_comment, name='delete_comment'),
]
