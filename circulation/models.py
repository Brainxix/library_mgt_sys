from django.db import models


class BorrowTransaction(models.Model):
    member = models.ForeignKey(
        "members.Member",
        on_delete=models.CASCADE,
    )

    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
    )

    borrowed_date = models.DateField(
        null=True,
        blank=True,
    )

    due_date = models.DateField(
        null=True,
        blank=True,
    )

    returned_date = models.DateField(
        null=True,
        blank=True,
    )

    STATUS_CHOICES = [
        ("BORROWED", "Borrowed"),
        ("RETURNED", "Returned"),
        ("OVERDUE", "Overdue"),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="BORROWED",
    )

    def __str__(self):
        return f"{self.member} borrowed {self.book}"