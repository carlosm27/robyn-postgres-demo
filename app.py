from robyn import Robyn, jsonify
from handlers import create_items, all_items
import json
from models import Items

from dotenv import load_dotenv

import os
import psycopg2

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

@app.get("/books")
async def books(request):
  
    conn = get_db_connection()
    
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    print(books)
    cur.close()
    conn.close()
    

    return books

@app.post("/book")
async def new_item(request,):
    body = bytearray(request['body']).decode("utf-8")
    json_body = json.loads(body)

    title = json_body['title']
    author = json_body['author']
    pages_num = json_body['pages_num']
    review = json_body['review']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO books (title, author, pages_num, review)'
                    'VALUES (%s, %s, %s, %s)',
                    (title, author, pages_num, review))
    conn.commit()
    cur.close()
    conn.close()

    
    return "Book Added"


    
    
    

    
    
    return {"status_code":201, "body": jsonify(new_item.__dict__['name']), "type": "json"}


app.start(port=8000, url="0.0.0.0")