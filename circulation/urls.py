from django.urls import path
from . import views

urlpatterns = [
    path("borrow/", views.borrow_book, name="borrow_book")
]
