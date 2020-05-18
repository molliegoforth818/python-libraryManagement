import sqlite3
from django.shortcuts import render
from libraryapp.models import Book
from ..connection import Connection


def book_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:

            conn.row_factory = model_factory(Book)

            db_cursor = conn.cursor()
            db_cursor.execute("""
            select
                b.id,
                b.title,
                b.isbn,
                b.author,
                b.year_published,
                b.publisher,
                b.librarian_id,
                b.library_id
            from libraryapp_book b
            """)

            all_books = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                book = Book()
                book.id = row['id']
                book.title = row['title']
                book.isbn = row['isbn']
                book.author = row['author']
                book.publisher = row['publisher']
                book.year_published = row['year_published']
                book.librarian_id = row['librarian_id']
                book.library_id = row['library_id']

                all_books.append(book)

        template = 'books/book_list.html'
        context = {
            'all_books': all_books
        }

        return render(request, template, context)