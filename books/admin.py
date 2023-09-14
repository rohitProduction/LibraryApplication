from django.contrib import admin
from .models import User, Book, Borrow

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Configuration of the admin interface for users."""
    list_display = [
        'username',
    ]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'title','description','image'
    ]

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = [
        'user','book','expectedDue'
    ]
