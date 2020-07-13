from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.home, name='tutor-home'),
    path('about/', views.about, name='tutor-about'),
    path('browse_tutors/', ProfileListView.as_view(), name='tutor-browseTutors'),
    path('404/', views.error404, name='test-404'),
    # path('user/<str:username>', UserPostListView.as_view(), name='user-profile'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    # path('post/new/', PostCreateView.as_view(), name='post-create'),
    # path('profile/<int:pk>/update/', ProfileUpdateView.as_view(), name='profile-update'),
    # path('profile/<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile-delete'),
]
