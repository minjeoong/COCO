from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/new/', views.new, name='new'),
    path('blog/create/', views.create, name='create'),
    path('blog/edit/<int:blog_id>/', views.edit, name='edit'),
    path('blog/update/<int:blog_id>/', views.update, name='update'),
    path('blog/delete/<int:blog_id>/', views.delete, name='delete'),
    path('blog/comment/<int:blog_id>/', views.add_comment_to_post, name='add_comment_to_post'),
    path('blog/<int:blog_id>/', views.detail, name='detail'),
    path('blog/like/<int:blog_id>/', views.like, name="like"),
    path('blog/product/', views.product, name="product"),
    path('blog/ingredient/', views.ingredient, name="ingredient"),
    path('blog/etc/', views.etc, name="etc"),
]
