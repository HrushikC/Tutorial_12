from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    # path('user/<str:username>', UserPostListView.as_view(), name='user-profile'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'), # change pk to username later. Also need to overwrite get_object() for Detail View
    # path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('404/', views.error404, name='test-404'),
]
