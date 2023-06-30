from django.contrib import admin
from .models import Mypage, MypageArticle, Comment, Liked
# Register your models here.
admin.site.register(Mypage)
admin.site.register(MypageArticle)
admin.site.register(Comment)
admin.site.register(Liked)