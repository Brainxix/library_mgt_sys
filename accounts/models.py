from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ("MEMBER", "Member"),
        ("LIBRARIAN", "Librarian"),
        ("ADMIN", "Administrator"),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="MEMBER")
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)