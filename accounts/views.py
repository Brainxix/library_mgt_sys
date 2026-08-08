
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .decorators import (member_required,librarian_required,admin_required,)

from .forms import RegisterForm, ProfileUpdateForm


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()
            login(request, user)

            if user.role == "ADMIN":
                return redirect("admin_dashboard")
            elif user.role == "LIBRARIAN":
                return redirect("librarian_dashboard")
            else:
                return redirect("member_dashboard")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.role == "ADMIN":
                return redirect("admin_dashboard")
            elif user.role == "LIBRARIAN":
                return redirect("librarian_dashboard")
            else:
                return redirect("member_dashboard")
    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def profile_view(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(
        request,
        "accounts/profile.html",
        {
            "user": request.user,
            "form": form,
        },
    )


@login_required
def member_dashboard(request):
    return render(request, "dashboard/member_dashboard.html")


@login_required
def librarian_dashboard(request):
    return render(request, "dashboard/librarian_dashboard.html")


@login_required
def admin_dashboard(request):
    return render(request, "dashboard/admin_dashboard.html")

