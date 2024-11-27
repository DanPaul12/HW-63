from sqlalchemy.orm import Session
from models.models import db
from models.models import Product

def save(product_data):
    with Session(db.engine) as session:
        with session.begin():
            product = Product(name=product_data['name'], price=product_data['price'])
            session.add(product)
            session.commit()
        session.refresh(product)
        return product