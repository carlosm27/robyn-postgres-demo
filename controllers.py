from dotenv import load_dotenv
import os
from init_db import conn
import psycopg2


load_dotenv()
USER = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

def get_db_connection():
    conn = psycopg2.connect(
        dbname = "robyn_db",
        user = "postgres",
        password = PASSWORD
    )

    return conn

def all_books():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    print(books)
    cur.close()
    conn.close()
    

    return books


def new_book(title:str, author:str, pages_num:int, review:str):
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO books (title, author, pages_num, review)'
                    'VALUES (%s, %s, %s, %s)',
                    (title, author, pages_num, review))
    conn.commit()
    cur.close()
    conn.close()

    
    return "Book Added"

def book_by_id(id:int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books WHERE id=%s', (id,))
    book = cur.fetchall()
    print(book)
    cur.close()
    conn.close()
    return book
