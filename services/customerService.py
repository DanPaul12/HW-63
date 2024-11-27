from sqlalchemy.orm import Session
from models.models import db
from models.models import Customer
from sqlalchemy import select

def save(new_customer):
    with Session(db.engine) as session:
        with session.begin():
            customer = Customer(name = new_customer['name'], email= new_customer['email'], phone= new_customer['phone'])
            session.add(customer)
            session.commit()
        session.refresh(customer)
        return customer 

def find_all():
    query = select(Customer)
    customers = db.session.execute(query).scalars().all()
    return customers