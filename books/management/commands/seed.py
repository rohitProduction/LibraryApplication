from django.core.management.base import BaseCommand, CommandError
from books.models import Book

class Command(BaseCommand):
    """The database seeder."""
    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        print('seeding data...')
        self.generateBooks()
        print('done.')

    def generateBooks(self):
        bookList = []
        book1 = Book.objects.create(
            title = 'The Electronic Swagman',
            description = 'A vivid title for a book about graphic design',
            image = None
        )
        book2 = Book.objects.create(
            title = 'The Power of Now',
            description = 'The title is the message here.',
            image = None
        )
        book3 = Book.objects.create(
            title = 'Lean In',
            description = 'This book was published less than a year ago and already the term ‘Lean in’ has become a widely used for female empowerment and success.',
            image = None
        )
        book4 = Book.objects.create(
            title = 'The Brain That Changes Itself',
            description = 'A breakthrough book that debunks the idea that a damaged brain can not be healed.',
            image = None
        )
        bookList.append(book1)
        bookList.append(book2)
        bookList.append(book3)
        bookList.append(book4)

        for book in bookList:
            print(book.title)
            book.full_clean()
            book.save()
