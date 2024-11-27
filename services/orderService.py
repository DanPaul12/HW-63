from sqlalchemy.orm import Session
from models.models import db
from models.models import Order
from sqlalchemy import select

def save(order_data):
    with Session(db.engine) as session:
        with session.begin():
            new_order = Order(customer_id=order_data['customer_id'], product_id=order_data['product_id'], quantity=order_data['quantity'], total_price=order_data['total_price'])
            