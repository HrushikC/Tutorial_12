from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.home, name='tutor-home'),
    path('about/', views.about, name='tutor-about'),
    path('browse/', BrowseProfilesView.as_view(), name='tutor-browse'),
    path('list/', MyTutorsListView.as_view(), name='tutor-list'),
    path('404/', views.error404, name='test-404'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/<int:pk>/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/create/', ProfileCreateView.as_view(), name='profile-create'),
    # path('profile/<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile-delete'),
]
