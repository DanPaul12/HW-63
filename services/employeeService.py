from sqlalchemy.orm import Session
from models.models import db
from models.models import Employee
from sqlalchemy import select

def save(employee_data):
    with Session(db.engine) as session:    #what does with Session and db.engine do?
        with session.begin():
            new_employee = Employee(name = employee_data['name'], position = employee_data['position'])
            session.add(new_employee)
            session.commit()
        session.refresh(new_employee)      #what does refresh do
        return new_employee

def find_all():
    query = select(Employee)         #why doesn't this one need "with session"
    employees = db.session.execute(query).scalars().all()
    return employees
