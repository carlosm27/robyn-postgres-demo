import collections
from datetime import datetime



def to_dict(psycopg_object:tuple):


    book_dict = collections.OrderedDict()
    book_dict['id'] = psycopg_object[0]
    book_dict['title'] = psycopg_object[1]
    book_dict['author'] = psycopg_object[2]
    book_dict['pages_num'] = psycopg_object[3]
    book_dict['review'] = psycopg_object[4]
    book_dict['datetime'] = psycopg_object[5].strftime("%m/%d/%Y")
    return book_dict

def list_dict(rows:list):

    row_list = []
    for row in rows:
        book_dict = to_dict(row)
        row_list.append(book_dict)

    return row_list    



