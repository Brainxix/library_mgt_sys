from django.db import models
from books.models import Book
from members.models import Member


class BorrowRecord(models.Model):
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )

    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        default="Borrowed"
    )

    def str(self):
        return f"{self.member} - {self.book}"