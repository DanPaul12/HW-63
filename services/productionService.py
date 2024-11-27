from sqlalchemy.orm import Session
from models.models import db
from models.models import Order, Customer, Product, Production
from sqlalchemy import select


def save(production_data):
    with Session(db.engine) as session:
        with session.begin():
            product_id = production_data['product_id']
            product = session.execute(select(Product).where(Product.id==product_id)).scalars().first()

            if not product:     #difference between if not product and product is none
                raise ValueError('no product')
            
            new_production= Production(product_id=production_data['product_id'], quantity_produced=production_data['quantity_produced'], date_produced=production_data['date_produced'])
            session.add(new_production)
            session.flush()
            session.commit()

        session.refresh(new_production)
        return new_production
    
def find_all():
    query = select(Production)
    productions = db.session.execute(query).scalars().all()
    return productions