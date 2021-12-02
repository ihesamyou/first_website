from django.shortcuts import get_object_or_404, redirect, render
from .models import User
from .forms import ProfileEditForm, RegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from blog.models import Comment


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'comments': Comment.objects.filter(author=user)
    }
    return render(request, 'users/profile.html', context)


@login_required
def profile_edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        context = {
            'user_form': UserEditForm(instance=request.user),
            'profile_form': ProfileEditForm(instance=request.user.profile)
        }
    return render(request, 'users/profile_edit.html', context)
