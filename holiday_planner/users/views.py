from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import os
from django.conf import settings


# user creation form already exists in django


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            """ Automatically hashes pw """
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Your account has been created! You are now able to log in.")
            return redirect("login")

    else:
        """ Empties the form """
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def remove_old_profile_picture(old_picture_path):
    os.remove(os.path.join(settings.BASE_DIR, "media", old_picture_path))


@login_required
def profile(request):
    current_image_path = str(User.objects.filter(username=request.user.username).first().profile.image)
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            if len(request.FILES) > 0:
                remove_old_profile_picture(current_image_path)
            user_form.save()
            profile_form.save()
            messages.success(request, f"Your account has been updated!")
            """ Need to redirect, in order to refresh data. post-get request """
            return redirect("profile")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'users/profile.html', context)


