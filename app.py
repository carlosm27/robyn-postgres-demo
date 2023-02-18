from robyn import Robyn
from controllers import all_books, new_book, book_by_id, delete_book, update_book
import json


app = Robyn(__file__)


@app.post("/book")
async def create_book(request):
    body = bytearray(request['body']).decode("utf-8")
    json_body = json.loads(body)

    title = json_body['title']
    author = json_body['author']
    pages_num = json_body['pages_num']
    review = json_body['review']

    book = new_book(title, author, pages_num, review)
    
    return book


@app.get("/books")
async def books():
    books = all_books()
    return books


@app.get("/book/:id")
async def get_book(request):
    id = request['params']['id']

    book = book_by_id(id)

    if book == None:
        return {"status_code":404, "body": "Book not Found", "type": "text"}
    else:
        return book   
    
        
@app.put("/book/:id")
async def update(request):
    id = request['params']['id']

    body = bytearray(request['body']).decode("utf-8")
    json_body = json.loads(body)

    title = json_body['title']
    author = json_body['author']
    pages_num = json_body['pages_num']
    review = json_body['review']

    book_id = book_by_id(id)

    if book_id == []:
        return {"status_code":404, "body": "Book not Found", "type": "text"}
    else:    
        book = update_book(title, author, pages_num, review, id)
        print(book)
        return book
    

@app.delete("/book/:id")
async def delete(request):
    id = request['params']['id']

    book = delete_book(id)

    if book != "Book deleted":
        return {"status_code":404, "body": "Book not Found", "type": "text"}
    else:    
        return book    



app.start(port=8000, url="0.0.0.0")