
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm


def book_list(request):
    books = Book.objects.all()
    return render(request, "books/book_list.html", {"books": books})


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
        form = BookForm(request.POST, request.FILES, instance=book,)
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
    return render(request, "books/book_detail.html",{
         "book":book
     })

