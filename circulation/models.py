from django.db import models
from books.models import Book
from members.models import Member
# Create your models here.

class BorrowTransaction(models.Model):
    member = models.ForeignKey(
        Member,on_delete=models.CASCADE
    )
    book = models.ForeignKey(
        Book,on_delete=models.CASCADE
    )
    borrowed_date = models.DateField(
        null=True, blank=True
    )
    due_date = models.DateField(
        null=True, blank=True
    )
    returned_date = models.DateField(
        null=True, blank=True
    )
    status_choices = [
        ("BORROWED", "Borrowed"),
        ("RETURNED","Returned"),
        ("OVERDUE", "Overdue"),
    ]
    
    status = models.CharField(
        max_length=20, choices= status_choices,default="BORROWED"
    )
    
    def __str__(self):
        return f"{self.member} borrowed{self.book}"
    