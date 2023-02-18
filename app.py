from robyn import Robyn, jsonify
from controllers import all_books, new_book, book_by_id
import json
from dotenv import load_dotenv
import os
import psycopg2
from init_db import conn


app = Robyn(__file__)


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



@app.get("/")
async def h(request):
    return "Hello, world!"


@app.post("/book")
async def create_book(request):
    body = bytearray(request['body']).decode("utf-8")
    json_body = json.loads(body)

    title = json_body['title']
    author = json_body['author']
    pages_num = json_body['pages_num']
    review = json_body['review']

    print(title)
    book = new_book(title, author, pages_num, review)
    print(book)
    
    return book

@app.get("/books")
async def books(request):
    print("Here")
    books = all_books()
    print(books)
    return books

@app.get("/book/:id")
async def get_book(request):
    id = request['params']['id']
    book_id = int(id)
    print(id)

    book = book_by_id(id)

    if book == []:
        return {"status_code":404, "body": "Book not Found", "type": "text"}
    else:    
        return book




    
    
    


app.start(port=8000, url="0.0.0.0")