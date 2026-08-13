from django.urls import path
from . import views


urlpatterns = [
    path("admin/", views.admin_dashboard, name="admin_dashboard"),
    
    path("librarian/", views.librarian_dashboard, name="librarian_dashboard"),
    
    path("member/", views.member_dashboard, name="member_dashboard"),
    
    path("my-borrowed-books/",views.my_borrowed_books,name="my_borrowed_books",),
    
    path("borrowing-history/",views.borrowing_history,name="borrowing_history",),
]