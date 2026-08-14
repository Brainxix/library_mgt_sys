from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Book, Category
from .forms import BookForm


def book_list(request):
    books = Book.objects.all()

    # Search & Filters
    query = request.GET.get("q")
    category = request.GET.get("category")
    status = request.GET.get("status")
    sort = request.GET.get("sort", "newest")

    # Search
    if query:
        books = books.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(isbn__icontains=query)
        )

    # Category Filter
    if category:
        books = books.filter(category_id=category)

    # Status Filter
    if status:
        books = books.filter(status=status)

    # Sorting
    if sort == "title":
        books = books.order_by("title")

    elif sort == "title_desc":
        books = books.order_by("-title")

    elif sort == "author":
        books = books.order_by("author")

    elif sort == "author_desc":
        books = books.order_by("-author")

    elif sort == "oldest":
        books = books.order_by("created_at")

    else:
        # Default: Newest first
        books = books.order_by("-created_at")
        
    total_books = Book.objects.count()

    available_books = Book.objects.filter(
        status="AVAILABLE"
    ).count()

    borrowed_books = Book.objects.filter(
        status="BORROWED"
    ).count()

    featured_books = Book.objects.filter(
        featured=True
    ).count()

    context = {
        "books": books,
        "query": query,
        "categories": Category.objects.all(),
        "status_choices": Book.STATUS,
        "sort": sort,
        
        "total_books": total_books,
        "available_books": available_books,
        "borrowed_books": borrowed_books,
        "featured_books": featured_books,
    }

    return render(request, "books/book_list.html", context)


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("book_list")
        else:
            print(form.errors)
    else:
        form = BookForm()

    return render(request, "books/book_form.html", {"form": form})


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)

    return render(request, "books/book_form.html", {"form": form})


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect("book_list")

    return render(request, "books/book_confirm_delete.html", {"book": book})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    return render(
        request,
        "books/book_detail.html",
        {
            "book": book
        }
    )
    
def digital_library(request):
    books = Book.objects.filter(
        digital_file__isnull=False
    ).exclude(
        digital_file=""
    ).order_by("-created_at")

    query = request.GET.get("q")

    if query:
        books = books.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(isbn__icontains=query)
        )

    context = {
        "books": books,
        "query": query,
    }

    return render(
        request,
        "books/digital_library.html",
        context
    )