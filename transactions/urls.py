from django.urls import path

from . import views


urlpatterns = [
    path(
        "issue/",
        views.issue_book,
        name="issue_book"
    ),
    
    path(
        "receive/<int:pk>/",
        views.receive_book,
        name="receive_book"
    ),
    
    path(
        "borrowed/",
        views.borrowed_books,
        name="borrowed_books"
    ),
    path(
        "overdue/",
        views.overdue_books,
        name="overdue_books"
    ),
]