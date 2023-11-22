# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment, PostLike
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import CommentForm, PostForm


class Homeview(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "app/home.html")


from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'app/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', None)
        filter_by_author = self.request.GET.get('author', None)

        # Apply search filter
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        # Apply author filter
        if filter_by_author:
            queryset = queryset.filter(author__username=filter_by_author)

        return queryset



class LikePostView(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        existing_like = PostLike.objects.filter(post=post, author=request.user).first()
        
        if existing_like:
            if existing_like.like_status:
                return redirect('app:post-list')

            existing_like.like_status = True
            existing_like.save()
        else:
            PostLike.objects.create(post=post, author=request.user, like_status=True)

        post.like_count += 1
        post.dislike_count = max(0, post.dislike_count - 1)
        post.save()

        return redirect('app:post-list')


class DislikePostView(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        existing_like = PostLike.objects.filter(post=post, author=request.user).first()

        if existing_like:
            if not existing_like.like_status:
                return redirect('app:post-list')
            
            existing_like.like_status = False
            existing_like.save()
        else:
            PostLike.objects.create(post=post, author=request.user, like_status=False)

        post.dislike_count += 1
        post.like_count = max(0, post.like_count - 1)
        post.save()

        return redirect('app:post-list')


class PostDetailView(DetailView):
    model = Post
    template_name = 'app/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = Comment.objects.filter(post=post)
        context['post_likes'] = PostLike.objects.filter(post=post)
        context['comment_form'] = CommentForm()  # Include the CommentForm in the context
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()

        comment_form = CommentForm(request.POST)  # Use the CommentForm

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment has been added.')

        return redirect('app:post-detail', pk=post.pk)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'app/post_create.html'
    form_class = PostForm
    success_url = '/app/posts/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        super().form_valid(form)
        return redirect('app:post-list')


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'app/post_update.html'
    form_class = PostForm


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'app/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
