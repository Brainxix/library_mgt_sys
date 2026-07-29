from django.shortcuts import render
from books.models import Book, Category


def home(request):

    featured_books = Book.objects.filter(featured=True)[:4]

    recent_books = Book.objects.order_by("-created_at")[:3]

    categories = Category.objects.all()

    context = {
        "featured_books": featured_books,
        "recent_books": recent_books,
        "categories": categories,
        "total_books": Book.objects.count(),
        "total_categories": Category.objects.count(),
        "available_books": Book.objects.filter(
            available_copies__gt=0
        ).count(),
    }

    return render(request, "core/home.html", context)