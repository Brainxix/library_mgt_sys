
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from books.models import Book
from members.models import Member

from accounts.decorators import (
    admin_required,
    librarian_required,
    member_required,
)


def dashboard_stats():
    return {
        "total_books": Book.objects.count(),
        "total_members": Member.objects.count(),
        "available_books": Book.objects.filter(
            available_copies__gt=0
        ).count(),
        "borrowed_books": Book.objects.filter(
            available_copies__lt=1
        ).count(),
    }


@login_required
@admin_required
def admin_dashboard(request):
    total_books = Book.objects.count()
    
    total_member = Member.objects.count()
    
    available_books = Book.objects.filter(available_copies__gt=0).count()
    borrowed_books = Book.objects.filter(available_copies__lt=1).count()
    recent_transactions = (Transactions.objects.select_related("book","member").order_by("-borrow_date")[:5])
    
    context = {
        "today": timezone.now(),
        "total_books": total_books,
        "total_members": total_member,
        "available_books": available_books,
        "borrowed_books": borrowed_books,
        "recent_transactions": recent_transactions,
    }
    return render(request, "dashboard/admin_dashboard.html", context)


@login_required
@librarian_required
def librarian_dashboard(request):
    context = dashboard_stats()
    return render(request, "dashboard/librarian_dashboard.html", context)


@login_required
@member_required
def member_dashboard(request):
    context = {
        "borrowed_books": Book.objects.filter(
            available_copies__lt=1
        ).count()
    }
    return render(request, "dashboard/member_dashboard.html", context)

