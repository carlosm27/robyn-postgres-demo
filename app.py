from robyn import Robyn, jsonify
from controllers import all_books, new_book, book_by_id, delete_book, update_book
import json
from models import Book


app = Robyn(__file__)


@app.post("/book")
async def create_book(request):
    body = bytearray(request['body']).decode("utf-8")
    json_body = json.loads(body)

    try:
        book = new_book(json_body['title'], json_body['author'])
        return {"status_code":201, "body": book, "type": "json"}
    except:
        return {"status_code":500, "body": "Internal Server Error", "type": "text"}


@app.get("/books")
async def books():
    books = all_books()
    return {"status_code":200, "body": books, "type": "json"}


@app.get("/book/:id")
async def get_book(request):
    id = request['params']['id']

    book = book_by_id(id)

    try:
        if book == None:
            return {"status_code":404, "body": "Book not Found", "type": "text"}
        else:
            return {"status_code":200, "body": book, "type": "json"}
    except:
         return {"status_code":500, "body": "Internal Server Error", "type": "text"}    
        
        
@app.put("/book/:id")
async def update(request):
    id = request['params']['id']

    body = bytearray(request['body']).decode("utf-8")
    json_body = json.loads(body)

    title = json_body['title']
    author = json_body['author']

    book_id = book_by_id(id)

    if book_id == None:
        return {"status_code":404, "body": "Book not Found", "type": "text"}
    else:
        try: 
            book = update_book(title, author, id)
            return {"status_code":200, "body": book, "type": "json"}
        except:
            return {"status_code":500, "body": "Internal Server Error", "type": "text"}
    

@app.delete("/book/:id")
async def delete(request):
    id = request['params']['id']

    book_id = book_by_id(id)

    if book_id == None:
        return {"status_code":404, "body": "Book not Found", "type": "text"}
    else:
        try: 
            delete_book(id)
            return {"status_code":200, "body": "Book deleted", "type": "json"}
        except:
            return {"status_code":500, "body": "Internal Server Error", "type": "text"}  



app.start(port=8000, url="0.0.0.0")