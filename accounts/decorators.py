from django.shortcuts import redirect
from django.contrib import messages


def member_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == "MEMBER":
            return view_func(request, *args, **kwargs)

        messages.error(request, "You don't have permission to access this page.")
        return redirect("login")

    return wrapper


def librarian_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == "LIBRARIAN":
            return view_func(request, *args, **kwargs)

        messages.error(request, "You don't have permission to access this page.")
        return redirect("login")

    return wrapper


def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == "ADMIN":
            return view_func(request, *args, **kwargs)

        messages.error(request, "You don't have permission to access this page.")
        return redirect("login")

    return wrapper