from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, RegexValidator
from datetime import datetime, timedelta

class User(AbstractUser):
    """User model used for authentication."""

    username = models.CharField(unique=True, blank=False, max_length=50)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(unique=True, blank=False)

    def __str__(self):
        return self.username

    def borrowBook(self, book):
        borrow = Borrow(user = self, book = book)
        borrow.save()


class Book(models.Model):
    title = models.CharField(max_length=50, unique=True, blank=False)
    description = models.CharField(max_length=520, blank=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title

    class meta:
        ordering = ['created_at']

class Borrow(models.Model):
    """Model to see which users have borrowed which books through foreign keys"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    expectedDue = models.DateField(default=datetime.now() + timedelta(days=7))

