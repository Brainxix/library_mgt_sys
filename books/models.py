from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):

    BOOK_TYPES = (
        ("PHYSICAL", "Physical"),
        ("DIGITAL", "Digital"),
        ("BOTH", "Physical & Digital"),
    )

    STATUS = (
        ("AVAILABLE", "Available"),
        ("BORROWED", "Borrowed"),
        ("RESERVED", "Reserved"),
    )

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=250, blank=True)

    author = models.CharField(max_length=150)

    isbn = models.CharField(max_length=20, unique=True)

    publisher = models.CharField(max_length=150, blank=True)

    publication_year = models.PositiveIntegerField()

    edition = models.CharField(max_length=50, blank=True)

    language = models.CharField(max_length=50, default="English")

    description = models.TextField(blank=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="books"
    )

    cover_image = models.ImageField(
        upload_to="books/covers/",
        blank=True,
        null=True
    )

    digital_file = models.FileField(
        upload_to="books/files/",
        blank=True,
        null=True
    )

    shelf_location = models.CharField(max_length=50, blank=True)

    total_copies = models.PositiveIntegerField(default=1)

    available_copies = models.PositiveIntegerField(default=1)

    book_type = models.CharField(
        max_length=20,
        choices=BOOK_TYPES,
        default="PHYSICAL"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="AVAILABLE"
    )

    featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

