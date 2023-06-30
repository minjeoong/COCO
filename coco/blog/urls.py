from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),  # 기본 home 경로
    path('category/<category_name>/', views.home, name='category_home'),  # 카테고리 선택 경로
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('edit/<int:blog_id>/', views.edit, name='edit'),
    path('update/<int:blog_id>/', views.update, name='update'),
    path('delete/<int:blog_id>/', views.delete, name='delete'),
    path('add_comment/<int:blog_id>/', views.add_comment, name='add_comment'),
    path('update_comment/<int:comment_id>/', views.update_comment, name='update_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    # path('blog/comment/<int:blog_id>/', views.add_comment_to_post, name='add_comment_to_post'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('like_blog/<int:blog_id>/', views.like_blog, name="like_blog"),
    # path('blog/product/', views.product, name="product"),
    # path('blog/ingredient/', views.ingredient, name="ingredient"),
    # path('blog/etc/', views.etc, name="etc"),
]