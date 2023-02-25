from init_db import get_db_connection
import json
from helpers import to_dict, list_dict
from models import Book


def all_books():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = list_dict(cur.fetchall())
    print(books)
    cur.close()
    conn.close()
    
    return json.dumps(books)


def new_book(title:str, author:str):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO books (title, author)'
                    'VALUES (%s, %s) RETURNING *;',
                    (title, author))
    book = cur.fetchone()[:]
    book_dict = to_dict(book)
    conn.commit()
    cur.close()
    conn.close()
    
    return json.dumps(book_dict)


def book_by_id(id:int):
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:

        cur.execute('SELECT * FROM books WHERE id=%s', (id,))
        book = cur.fetchone()
        book_dict = to_dict(book)
        

        cur.close()
        conn.close()
        return json.dumps(book_dict)
    except:
        return None



def update_book(title:str, author, id:int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE books SET title = %s, author=%s WHERE id = %s RETURNING *;', (title, author, id))
    book = cur.fetchone()[:]
    book_dict = to_dict(book)
    
    conn.commit()
    cur.close()
    conn.close()
  
    return  json.dumps(book_dict)


def delete_book(id:int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s", (id))
    conn.commit()
    conn.close()

    return "Book deleted"

