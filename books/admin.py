from django.contrib import admin

from .models import Book, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "category",
        "book_type",
        "status",
        "available_copies",
    )

    list_filter = (
        "category",
        "book_type",
        "status",
        "featured",
    )

    search_fields = (
        "title",
        "author",
        "isbn",
    )

    list_editable = (
        "status",
    )

