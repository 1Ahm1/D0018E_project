from jsql import sql

from fastapi import  status
from domain.utils.general import UserInfo,BookInfo
from api import app

def create_book(conn, user_info: UserInfo, data: BookInfo):

    is_here = sql(
        conn,
        """
            SELECT COUNT(*) FROM `book`
            WHERE `name` = :name
        """,
        name = data.name
    ).scalar()
    if is_here == 0:
        sql(
        conn,
        """
            Insert INTO book (user_id, name, author, description)
            VALUES (:user_id, :name, :author, :description)
        """,
        author = data.author,
        name = data.name,
        description = data.description,
        book_id = data.book_id
    ).lastrowid
    

def delet_book(conn, user_info: UserInfo, book_id):

    is_here = sql(
        conn,
        """
            SELECT COUNT(*) FROM `book`
            WHERE `book_id` = :id
        """,
        id = book_id
    ).scalar()
    if is_here != 0:
        sql(
        conn,
        """
            DELETE FROM book
            WHERE `book_id` = :id
        """,
        id = book_id
        
    ).lastrowid
    
    
def book_details(conn, book_id):
    data = sql(
        conn,
        """
            SELECT book_id, name, author, description
            FROM book
            WHERE book_id =:book_id 
        """,
        book_id = book_id
    ).dict()    
    return data