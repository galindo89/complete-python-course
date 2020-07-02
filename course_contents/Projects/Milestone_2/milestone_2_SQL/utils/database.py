import sqlite3 #Import SQL lite3
from utils.database_connection import DatabaseConnection

# with sqlite3.connect("data.db") as connection:
#     cursor=connection.cursor()
#     cursor.execute("Your SQL Query Here")
#     connection.commit()

def create_book_table():
    with DatabaseConnection("data.db") as connection:
    # connection=sqlite3.connect("data.db")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS books(name text,author text,read integer)")
        # connection.commit()
        # connection.close()



def get_all_books():
    with DatabaseConnection("data.db") as connection:
    # connection=sqlite3.connect("data.db")
        cursor=connection.cursor()
        cursor.execute("SELECT * from books")
        books=[dict(zip(["name", "author", "read"],book)) for book in cursor.fetchall()]
        return books

def add_book(name, author):
    with DatabaseConnection("data.db") as connection:
    # connection=sqlite3.connect("data.db")
        cursor=connection.cursor()
        cursor.execute("INSERT INTO books VALUES(?,?,0)",(name,author))
    # connection.commit()
    # connection.close()

def mark_book_as_read(name):
    with DatabaseConnection("data.db") as connection:
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE books SET read=1 WHERE name=?",(name,))
    # connection.commit()
    # connection.close()


def delete_book(name):
    with DatabaseConnection("data.db") as connection:
    # connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM books WHERE name=?",(name,))
    # connection.commit()
    # connection.close()


