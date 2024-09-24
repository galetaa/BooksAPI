import psycopg2
from psycopg2.extras import RealDictCursor
from utils import retry


def connect_db():
    conn = psycopg2.connect(
        dbname="book_management_db",
        user="book_user",
        password="password",
        host="localhost",
        port="5432"
    )
    return conn


@retry(times=3, delay=2, exceptions=(psycopg2.DatabaseError,))
def get_book_by_id(book_id):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM books_book WHERE id = %s", (book_id,))
        return cursor.fetchone()
    except psycopg2.DatabaseError as e:
        print(f"Database error: {str(e)}")
        raise
    finally:
        cursor.close()
        conn.close()


def get_all_books():
    conn = connect_db()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM books_book")
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return books
