from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

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


@login_required
def profile(request):
    return render(request, 'users/profile.html')