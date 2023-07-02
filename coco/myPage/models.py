from django.db import models
from user.models import CustomUser

class Mypage(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    mainImage = models.ImageField(upload_to='mypage/', null=True)
    subImage1 = models.ImageField(upload_to='mypage/', null=True)
    subImage2 = models.ImageField(upload_to='mypage/', null=True)
    subImage3 = models.ImageField(upload_to='mypage/', null=True)
    # 다대다 관계를 위해 Mypage 모델에 content 필드는 필요하지 않습니다.

    def __str__(self):
        return f"Mypage for {self.user.username}"

class MypageArticle(models.Model):
    mypage = models.ForeignKey(
        Mypage, on_delete=models.CASCADE, related_name='contents')
    title = models.CharField(max_length=20)
    content_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='mypage/articleImage/', null=True)
    def __str__(self):
        return f"글 내용: {self.content_text}"

class Liked(models.Model):
    article = models.ForeignKey(
        MypageArticle, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"Liked: {self.user.username} liked {self.article}"

class Comment(models.Model):
    article = models.ForeignKey(MypageArticle, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment: {self.user.username} commented on {self.article}"
