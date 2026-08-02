from django import forms
from .models import BorrowTransaction

class BorrowTransactionForm(forms.ModelForm):
    class Meta:
        model = BorrowTransaction
        fields = [
            "member",
            "book",
            "due_date",
            "borrowed_date",
        ]