from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=150)
    isbn= models.CharField(max_length=20,unique=True)
    category= models.CharField(max_length=150)
    number_of_pages=models.PositiveIntegerField("")
    quantity=models.PositiveIntegerField("default=1")
    available=models.PositiveIntegerField("default=1")
    
    def __str__(self):
        return self.title 
    
