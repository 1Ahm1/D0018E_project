from jsql import sql

from fastapi import  status
from domain.utils.general import UserInfo,BookInfo,ProductInfo
from api import app

def create_product(conn, user_info: UserInfo, data: ProductInfo):

    is_here = sql(
        conn,
        """
            SELECT COUNT(*) FROM `product`
            WHERE `name` = :name
        """,
        name = data.name
    ).scalar()
    if is_here == 0:
        sql(
        conn,
        """
            Insert INTO product (product_id, price, quantity, book_id)
            VALUES (:product_id, :price, :quantity, :book_id)
        """,
        product_id = data.product_id,
        price = data.price,
        quantity = data.quantity,
        book_id = data.book_id
    ).lastrowid
    

def delet_product(conn, user_info: UserInfo, product_id):

    is_here = sql(
        conn,
        """
            SELECT COUNT(*) FROM `product`
            WHERE `product_id` = :id
        """,
        id = product_id
    ).scalar()
    if is_here != 0:
        sql(
        conn,
        """
            DELETE FROM product
            WHERE `product_id` = :id
        """,
        id = product_id
        
    ).lastrowid
    
    
def product_details(conn, product_id):
    data = sql(
        conn,
        """
            SELECT product_id, price, quantity, book_id
            FROM product
            WHERE product_id =:product_id 
        """,
        product_id = product_id
    ).dict()    
    return data