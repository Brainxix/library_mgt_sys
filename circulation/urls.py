from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.borrowing_list,
        name="borrowing_list",
    ),

    path(
        "issue/",
        views.issue_book,
        name="issue_book",
    ),
    
    path(
    "return/<int:pk>/",
    views.return_book,
    name="return_book",
    ),
]