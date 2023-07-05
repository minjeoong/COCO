from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

app_name = 'myPage'
urlpatterns = [
    path('<int:user_id>/', login_required(myPage), name='myPage'),
    path('upload/', login_required(upload), name='upload'),
    path('newArticle/', login_required(newArticle), name='newArticle'),
    path('createArticle/', login_required(createArticle), name='createArticle'),
    path('detailArticle/<int:article_id>/', login_required(detailArticle), name='detailArticle'),
    path('editArticle/<int:article_id>/', login_required(editArticle), name='editArticle'),
    path('updateArticle/<int:article_id>/', login_required(updateArticle), name='updateArticle'),
    path('deleteArticle/<int:article_id>/', login_required(deleteArticle), name='deleteArticle'),
    path('like/<int:article_id>/', login_required(like_article), name='like_article'),
    path('create_comment/<int:article_id>/',login_required(create_comment), name='create_comment'),
    path('update_comment/<int:comment_id>/',login_required(update_comment), name='update_comment'),
    path('delete_comment/<int:comment_id>/',login_required(delete_comment), name='delete_comment'),
]
