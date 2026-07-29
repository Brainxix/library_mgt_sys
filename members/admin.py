from django.contrib import admin
from .models import Member

# Register your models here.



@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "phone",
        "joined_date",
    )

    search_fields = (
        "first_name",
        "last_name",
        "email",
    )

