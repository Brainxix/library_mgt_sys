
from django.urls  import path
from . import views
urlpatterns = [
    path("", views.book_list, name="book_list"),
    
    path("add/", views.add_book, name="book_create"),
    
    path("edit/<int:pk>/", views.edit_book, name="edit_book"),
    
    path("delete/<int:pk>/", views.delete_book, name="delete_book"),
    
    path("<int:pk>/", views.book_detail, name="book_detail"),

]