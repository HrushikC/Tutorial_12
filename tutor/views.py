from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
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


# def browse_tutors(request):  # make ListView version of this method later
#     profiles = TutorProfile.objects.all()
#     profiles = profiles.filter(is_hidden=False)
#     profiles = profiles.order_by('-date_posted')  # order by something else in future
#
#     filter_results = TutorFilter(request.GET, profiles)
#
#     paginator = Paginator(filter_results.qs, 5)  # Show 5 profiles per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     context = {
#         'page_obj': page_obj,
#         'filter': filter_results
#     }
#
#     return render(request, 'tutor/browse_tutors.html', context)


class BrowseProfilesView(ListView):
    model = TutorProfile
    template_name = 'tutor/browse_tutors.html'  # <app>/<model>_<viewtype>.html

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        profiles = TutorProfile.objects.filter(is_hidden=False).order_by('-date_posted')
        profiles = profiles.order_by('-date_posted')  # order by something else in future
        filter_results = TutorFilter(self.request.GET, profiles)
        paginator = Paginator(filter_results.qs, 5)  # Show 5 profiles per page
        page_number = self.request.GET.get('page')
        context['page_obj'] = paginator.get_page(page_number)
        context['filter'] = filter_results
        return context


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

    def get_object(self, *args, **kwargs):
        return get_object_or_404(TutorProfile, user_id=self.kwargs['pk'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        account = Account.objects.get(user_id=self.request.user.id)
        if 'add' in self.request.GET:
            account.tutorprofiles.add(self.get_object())
            messages.success(self.request, f"You have successfully added {self.get_object().user.username}'s "
                                           f"profile to \"My List\"")
        elif 'remove' in self.request.GET:
            account.tutorprofiles.remove(self.get_object())
            messages.success(self.request, f"You have successfully removed {self.get_object().user.username}'s "
                                           f"profile from \"My List\"")
        has_tutor = account.tutorprofiles.filter(user_id=self.get_object().user.id).count() > 0
        context['has_tutor'] = has_tutor
        return context


class ProfileCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = ProfileCreateForm
    template_name = 'tutor/tutorprofile_create_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        account = Account.objects.get(user_id=self.request.user.id)
        account.created_tutorprofile = True
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

