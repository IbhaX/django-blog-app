from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('', views.Homeview.as_view(), name="home"),
    
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/like/', views.LikePostView.as_view(), name='like-post'),
    path('posts/<int:pk>/dislike/', views.DislikePostView.as_view(), name='dislike-post'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/create/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]
