from django.contrib import admin
from .models import BorrowTransaction
# Register your models here.
@admin.register(BorrowTransaction)
class BorrowTransactionAdmin(admin.ModelAdmin):
    list_display = ( 
                    "member", 
                    "book",
                    "borrowed_date", 
                    "due_date", 
                    "returned_date", 
                    "status"
)
    list_filter = ("status",)
    search_fields= (
        "member__user_username",
        "book__title"
    )
    