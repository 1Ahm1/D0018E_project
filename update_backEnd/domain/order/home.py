from jsql import sql

from fastapi import  status
from domain.utils.general import UserInfo,OrderInfo
from api import app

def create_order(conn, user_info: UserInfo, data: OrderInfo):

    is_here = sql(
        conn,
        """
            SELECT COUNT(*) FROM `order`
            WHERE `order_id` = :id
        """,
        id = OrderInfo.order_id
    ).scalar()
    if is_here == 0:
        sql(
        conn,
        """
            Insert INTO order (order_id, price, quantity, product_id,customer_id,date)
            VALUES (:order_id, :price, :quantity, :product_id, :customer_id,:date)
        """,
        order_id = data.order_id,
        price = data.price,
        quantity = data.quantity,
        product_id = data.product_id,
        customer_id=data.customer_id,
        date=data.date
    ).lastrowid
    

def delet_order(conn, user_info: UserInfo, order_id):

    is_here = sql(
        conn,
        """
            SELECT COUNT(*) FROM `order`
            WHERE `order_id` = :id
        """,
        id = order_id
    ).scalar()
    if is_here != 0:
        sql(
        conn,
        """
            DELETE FROM order
            WHERE `order_id` = :id
        """,
        id = order_id
        
    ).lastrowid
    
    
def order_details(conn, order_id):
    data = sql(
        conn,
        """
            SELECT order_id, price, quantity, product_id, customer_id, date
            FROM order
            WHERE order_id =:order_id 
        """,
        order_id = order_id
    ).dict()    
    return data