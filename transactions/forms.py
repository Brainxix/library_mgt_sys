from django import forms
from django.utils import timezone

from .models import BorrowRecord
from books.models import Book


class BorrowRecordForm(forms.ModelForm):

    class Meta:
        model = BorrowRecord
        fields = ["member", "book", "due_date"]

        widgets = {
            "member": forms.Select(attrs={
                "class": "form-control"
            }),

            "book": forms.Select(attrs={
                "class": "form-control"
            }),

            "due_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["book"].queryset = Book.objects.filter(
            available_copies__gt=0
        )

        self.fields["due_date"].widget.attrs[
            "min"
        ] = timezone.now().date().isoformat()