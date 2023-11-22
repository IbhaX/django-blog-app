from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)
    

    
    
    def __str__(self) -> str:
        return self.comment

class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    like_status = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.post.title

class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    like_status = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.comment.comment
