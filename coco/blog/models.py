from django.db import models
from django.utils import timezone
from town.models import Town
from user.models import CustomUser
class TownBlog(models.Model):
    town = models.OneToOneField(Town, on_delete=models.CASCADE, related_name='blog')

def get_image_upload_path_blog(instance, filename):
    townname = instance.townblog.town.townname.lower().replace(" ", "_")
    return f"{townname}/blog/{instance.user.id}/{filename}"

class Blog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')
    townblog = models.ForeignKey(TownBlog, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    hit = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=10)
    image = models.ImageField(upload_to=get_image_upload_path_blog, null=True, blank=True)

    
    # 글 삭제 시 media 파일 동시 삭제
    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        super().delete(*args, **kwargs)

    class Meta:
        db_table = 'blog'
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:100]
    
    @property
    def update_counter(self):
        self.hit += 1
        self.save()
        return self.hit


class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    comment_text = models.TextField()

    def __str__(self):
        return f"Comment: {self.user.username}"

    class Meta:
        db_table = 'comment'

    def approve(self):
       self.save()

    
class BlogLike(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return f"Liked: {self.user.username}"