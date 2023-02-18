
from init_db import get_db_connection


def all_books():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    
    return books


def new_book(title:str, author:str, pages_num:int, review:str):

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO books (title, author, pages_num, review)'
                    'VALUES (%s, %s, %s, %s) RETURNING *;',
                    (title, author, pages_num, review))
    book = cur.fetchone()[:]
    conn.commit()
    cur.close()
    conn.close()
    
    return book


def book_by_id(id:int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books WHERE id=%s', (id,))
    book = cur.fetchone()
    
    cur.close()
    conn.close()
    return book


def update_book(title:str, author, pages_num, review, id:int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE books SET title = %s, author=%s, pages_num=%s, review=%s WHERE id = %s RETURNING *;', (title, author, pages_num, review, id))
    book =cur.fetchone()[:]
    conn.commit()
    cur.close()
    conn.close()
  
    return  book


def delete_book(id:int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s", (id))
    conn.commit()
    conn.close()

    return "Book deleted"
