from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import BorrowTransactionForm
from .models import BorrowTransaction


def issue_book(request):

    if request.method == "POST":
        form = BorrowTransactionForm(request.POST)

        if form.is_valid():
            transaction = form.save(commit=False)
            book = transaction.book

            if book.available_copies <= 0:
                messages.error(
                    request,
                    f'"{book.title}" is currently unavailable.'
                )

                return render(
                    request,
                    "circulation/borrow_book.html",
                    {"form": form},
                )

            transaction.save()

            book.available_copies -= 1

            if book.available_copies == 0:
                book.status = "BORROWED"
            else:
                book.status = "AVAILABLE"

            book.save(
                update_fields=[
                    "available_copies",
                    "status",
                    "updated_at",
                ]
            )

            messages.success(
                request,
                f'"{book.title}" was successfully issued.'
            )

            return redirect("borrowing_list")

    else:
        form = BorrowTransactionForm()

    return render(
        request,
        "circulation/borrow_book.html",
        {"form": form},
    )


def borrowing_list(request):
    transactions = BorrowTransaction.objects.all().order_by("-id")

    return render(
        request,
        "circulation/borrowing_list.html",
        {"transactions": transactions},
    )


def return_book(request, pk):
    transaction = get_object_or_404(
        BorrowTransaction,
        pk=pk
    )

    # Prevent returning the same book twice
    if transaction.status == "RETURNED":
        messages.warning(
            request,
            "This book has already been returned."
        )
        return redirect("borrowing_list")

    book = transaction.book

    # Mark transaction as returned
    transaction.returned_date = timezone.now().date()
    transaction.status = "RETURNED"
    transaction.save(
        update_fields=[
            "returned_date",
            "status",
        ]
    )

    # Restore available copy
    book.available_copies += 1

    if book.available_copies > 0:
        book.status = "AVAILABLE"

    book.save(
        update_fields=[
            "available_copies",
            "status",
            "updated_at",
        ]
    )

    messages.success(
        request,
        f'"{book.title}" was successfully returned.'
    )

    return redirect("borrowing_list")