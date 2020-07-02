from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import TutorProfile

def home(request):
    return render(request, 'tutor/home.html', {'title': 'Home'})

def browseTutors(request):
    content = {
        'profiles': TutorProfile.objects.all()
    }
    return render(request, 'tutor/browse_tutors.html', content)


class ProfileListView(ListView):
    model = TutorProfile
    template_name = 'tutor/browse_tutors.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'profiles'
    ordering = ['-date_posted']
    paginate_by = 5


# class UserPostListView(ListView):
#     model = TutorProfile
#     template_name = 'tutor/user_posts.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     paginate_by = 5
#
#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return TutorProfile.objects.filter(author=user).order_by('-date_posted')


class ProfileDetailView(DetailView):
    model = TutorProfile
    template_name = 'tutor/profile_detail.html'


# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = TutorProfile
#     fields = ['name', 'bio']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TutorProfile
    fields = ['name', 'bio']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TutorProfile
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'tutor/about.html', {'title': 'About'})

# Test 404. Temporary Path. Remove method when debug = true.
def error404(request):
    return render(request, 'tutor/404.html', {'title': 'Test-404'})

