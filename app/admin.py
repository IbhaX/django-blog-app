from django.contrib import admin
from .models import Post, Comment, PostLike, CommentLike


class CommentInline(admin.TabularInline):
    model = Comment


class PostLikeInline(admin.TabularInline):
    model = PostLike


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline, PostLikeInline]
    list_display = ['title', 'author']




