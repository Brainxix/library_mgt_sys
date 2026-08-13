from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone
from .forms import BorrowRecordForm
from .models import BorrowRecord

@login_required
def issue_book(request):

    if request.method == "POST":
        form = BorrowRecordForm(request.POST)

        if form.is_valid():

            borrow_record = form.save(commit=False)
            book = borrow_record.book

            if book.available_copies <= 0:
                messages.error(
                    request,
                    "This book is currently unavailable."
                )
                return redirect("issue_book")

            borrow_record.status = "Borrowed"
            borrow_record.save()

            book.available_copies -= 1

            if book.available_copies == 0:
                book.status = "BORROWED"
            else:
                book.status = "AVAILABLE"

            book.save()

            messages.success(
                request,
                f'"{book.title}" has been issued successfully.'
            )

            return redirect("librarian_dashboard")

    else:
        form = BorrowRecordForm()

    return render(
        request,
        "transactions/issue_book.html",
        {"form": form}
    )
    
@login_required
def receive_book(request, pk):
    try:
        borrow_record = BorrowRecord.objects.get(
            pk=pk,
            status="Borrowed"
        )
    except BorrowRecord.DoesNotExist:
        messages.error(
            request,
            "Borrow record not found or the book has already been returned."
        )
        return redirect("borrowed_books")

    if request.method == "POST":
        borrow_record.return_date = timezone.now().date()
        borrow_record.status = "Returned"
        borrow_record.save()

        book = borrow_record.book

        if book.available_copies < book.total_copies:
            book.available_copies += 1

        if book.available_copies > 0:
            book.status = "AVAILABLE"

        book.save()

        messages.success(
            request,
            f'"{book.title}" has been received successfully.'
        )

        return redirect("borrowed_books")

    return render(
        request,
        "transactions/receive_book.html",
        {"borrow_record": borrow_record}
    )
    
@login_required
def borrowed_books(request):
    records = BorrowRecord.objects.filter(
        status="Borrowed"
    ).select_related(
        "member",
        "book"
    ).order_by("-borrow_date")

    return render(
        request,
        "transactions/borrowed_books.html",
        {"records": records}
    )
@login_required
def overdue_books(request):
    today = timezone.now().date()
    records = BorrowRecord.objects.filter(
        status="Borrowed",
        due_date__lt=today
    ).select_related(
        "member",
        "book"
    ).order_by("due_date")
    
    for reord in records:
        record.days_overdue = (today - record.due_date).days

    return render(
        request,
        "transactions/overdue_books.html",
        {"records": records,
         }
    )