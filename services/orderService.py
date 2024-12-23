from sqlalchemy.orm import Session
from models.models import db
from models.models import Order, Customer, Product
from sqlalchemy import select

def save(order_data):
    with Session(db.engine) as session:
        with session.begin():
            customer_id = order_data['customer_id']
            customer = session.execute(select(Customer).where(Customer.id==customer_id)).scalars().first()

            product_id = order_data['product_id']
            product = session.execute(select(Product).where(Product.id==product_id)).scalars().first()

            if not customer:
                raise ValueError('no customer')
            
            if not product:
                raise ValueError('no product')
            
            new_order= Order(customer_id=order_data['customer_id'], product_id=order_data['product_id'], quantity= order_data['quantity'], total_price=order_data['total_price'])
            session.add(new_order)
            session.flush()
            session.commit()
        
        session.refresh(new_order)
        return new_order
    
def find_all():
    query = select(Order)
    orders = db.session.execute(query).scalars().all()
    return orders

def find_all_pagination(page, per_page):
    orders = db.paginate(select(Order), page=page, per_page=per_page)
    return orders
