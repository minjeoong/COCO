from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    hit = models.PositiveIntegerField(default=0)
    tag = models.ManyToManyField('Tag', blank=True)
    image = models.ImageField(upload_to='blog/', null=True)
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

class Comment(models.Model):
    post=models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    author_name=models.CharField(max_length=20)
    comment_text=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'comment'

    def approve(self):
       self.save()

    def __str__(self):
        return self.comment_text
    
class Tag(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'tag'

    def __str__(self):
        return self.name
    
class Like(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'like'
    
    def __str__(self):
        return self.blog.title