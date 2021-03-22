from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import TutorProfile, Subject
from users.models import Account
from .filters import TutorFilter
from .forms import ProfileCreateForm, ProfileUpdateForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    return render(request, 'tutor/home.html', {'title': 'Home'})


def browse_tutors(request):  # make ListView version of this method later
    profiles = TutorProfile.objects.all()
    profiles = profiles.filter(is_hidden=False)
    profiles = profiles.order_by('-date_posted')  # order by something else in future

    filter_results = TutorFilter(request.GET, profiles)

    paginator = Paginator(filter_results.qs, 5)  # Show 5 profiles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'filter': filter_results
    }

    return render(request, 'tutor/browse_tutors.html', context)


# class TutorProfileListView(ListView):
#     model = TutorProfile
#     template_name = 'tutor/browse_tutors.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'profiles'
#     ordering = ['-date_posted']
#     paginate_by = 5


# class UserPostListView(ListView):
#     model = TutorProfile
#     template_name = 'tutor/user_posts.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     paginate_by = 5
#
#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return TutorProfile.objects.filter(author=user).order_by('-date_posted')


class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'tutor/profile_detail.html'

    def get_object(self):
        return get_object_or_404(TutorProfile, user_id=self.kwargs['pk'])


class ProfileCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = ProfileCreateForm
    template_name = 'tutor/tutorprofile_create_form.html'

    def update_account(self):
        account = Account.objects.get(user_id=self.request.user.id)
        account.created_tutorprofile = True

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        tp = TutorProfile.objects.get(user_id=self.request.user.id)
        if not tp:
            return True
        return False


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = ProfileUpdateForm
    template_name = 'tutor/tutorprofile_update_form.html'

    def get_object(self):
        return get_object_or_404(TutorProfile, user_id=self.kwargs['pk'])

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        return False


# class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = TutorProfile
#     success_url = '/'
#
#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False


def about(request):
    return render(request, 'tutor/about.html', {'title': 'About'})


# Test 404. Temporary Path. Remove method when settings.debug = false.
def error404(request):
    return render(request, 'tutor/404.html', {'title': 'Test-404'})

