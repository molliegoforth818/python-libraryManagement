import sqlite3
from django.shortcuts import render
from libraryapp.models import Library, Book
from ..connection import Connection
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect

@login_required
def list_libraries(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = create_library
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT
                    li.id,
                    li.name,
                    li.address,
                    b.id book_id,
                    b.title book_title,
                    b.author,
                    b.publisher,
                    b.year_published,
                    b.isbn
                FROM libraryapp_library li
                JOIN libraryapp_book b ON li.id = b.library_id
            """)

            libraries = db_cursor.fetchall()

        library_groups = {}
        for (library, book) in libraries:
            if library.id not in library_groups:
                library_groups[library.id] = library
                library_groups[library.id].books.append(book)
            else:
                library_groups[library.id].books.append(book)
        template = 'libraries/list.html'
        context = {
            'all_libraries': library_groups.values()
        }

        return render(request, template, context)
    elif request.method == 'POST':
        form_data = request.POST

    with sqlite3.connect(Connection.db_path) as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO libraryapp_library
        (
            name, address
        )
        VALUES (?, ?)
        """,
        (form_data['name'], form_data['address']))

    return redirect(reverse('libraryapp:libraries'))

# def create_library(cursor, row):
#     _row = sqlite3.Row(cursor, row)
#     library = Library()
#     library.id = _row["id"]
#     library.name = _row["name"]
#     library.address = _row["address"]
#     library.books = []
#     book = Book()
#     book.id = _row["book_id"]
#     book.title = _row["book_title"]
#     book.author = _row["author"]
#     book.publisher = _row["publisher"]
#     book.year_published = _row["year_published"]
#     book.isbn = _row["isbn"]

#     return (library, book,)