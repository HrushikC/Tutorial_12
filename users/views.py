from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        a_form = AccountRegisterForm(request.POST)
        if form.is_valid() and a_form.is_valid():
            form.save()
            a_form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
        a_form = AccountRegisterForm()

    context = {
        'form': form,
        'a_form': a_form
    }
    return render(request, 'users/register.html', context)


@login_required
def account(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfilePicUpdateForm(request.POST, request.FILES, instance=request.user.account)
        t_form = AccountUpdateForm(request.POST, instance=request.user.account)

        if u_form.is_valid() and p_form.is_valid() and t_form.is_valid():
            u_form.save()
            p_form.save()
            t_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('account')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfilePicUpdateForm(instance=request.user.account)
        t_form = AccountUpdateForm(instance=request.user.account)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        't_form': t_form
    }

    return render(request, 'users/account.html', context)
