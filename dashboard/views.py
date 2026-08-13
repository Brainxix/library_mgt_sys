
from django.contrib.auth.decorators import login_required
from transactions.models import BorrowRecord
from django.shortcuts import render
from django.utils import timezone
from members.models import Member
from books.models import Book

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
            status="Borrowed"
        ).count(),
    }


@login_required
@admin_required
def admin_dashboard(request):
    context = dashboard_stats()

    context["today"] = timezone.now()
    
    context["recent_members"] = Member.objects.order_by("-id")[:5]

    return render(
        request,
        "dashboard/admin_dashboard.html",
        context,
    )


@login_required
@librarian_required
def librarian_dashboard(request):
    context = dashboard_stats()

    today = timezone.now().date()

    context["overdue_books"] = BorrowRecord.objects.filter(
        status="Borrowed",
        due_date__lt=today,
        return_date__isnull=True,
    ).count()

    context["recent_transactions"] = (
        BorrowRecord.objects
        .select_related("member", "book")
        .order_by("-borrow_date")[:5]
    )

    context["today"] = today

    return render(
        request,
        "dashboard/librarian_dashboard.html",
        context,
    )


@login_required
@member_required
def member_dashboard(request):
    context = {
        "borrowed_books": BorrowRecord.objects.filter(
            member__user=request.user,
            status="Borrowed",
        ).count(),
    }

    return render(
        request,
        "dashboard/member_dashboard.html",
        context,
)
    
@login_required
@member_required
def my_borrowed_books(request):
    records = (
        BorrowRecord.objects
        .filter(
            member__user=request.user,
            status="Borrowed",
        )
        .select_related("book")
        .order_by("due_date")
    )

    return render(
        request,
        "dashboard/my_borrowed_books.html",
        {
            "records": records,
            "today": timezone.now().date(),
        },
    )
    
@login_required
@member_required
def borrowing_history(request):
    records = (
        BorrowRecord.objects
        .filter(member__user=request.user)
        .select_related("book")
        .order_by("-borrow_date")
    )

    return render(
        request,
        "dashboard/borrowing_history.html",
        {
            "records": records,
        },
    )