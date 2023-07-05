from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
app_name = 'blog'

urlpatterns = [
    path('', login_required(home), name='home'),  # 기본 home 경로
    path('category/<category_name>/', login_required(home), name='category_home'),  # 카테고리 선택 경로
    path('new/', login_required(new), name='new'),
    path('create/', login_required(create), name='create'),
    path('edit/<int:blog_id>/', login_required(edit), name='edit'),
    path('update/<int:blog_id>/', login_required(update), name='update'),
    path('delete/<int:blog_id>/', login_required(delete), name='delete'),
    path('add_comment/<int:blog_id>/', login_required(add_comment), name='add_comment'),
    path('update_comment/<int:comment_id>/', login_required(update_comment), name='update_comment'),
    path('delete_comment/<int:comment_id>/', login_required(delete_comment), name='delete_comment'),
    path('<int:blog_id>/', login_required(detail), name='detail'),
    path('like_blog/<int:blog_id>/', login_required(like_blog), name="like_blog"),
]