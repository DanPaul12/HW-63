from sqlalchemy.orm import Session
from models.models import db
from models.models import Employee
from sqlalchemy import select
from circuitbreaker import circuit

def fallback_func(customer):
    return None

@circuit(failure_threshold=1, recovery_timeout=10, fallback_function=fallback_func)
def save(employee_data):
    with Session(db.engine) as session:    #what does with Session and db.engine do?
       try:
            if employee_data['name']== 'Failure':
                raise Exception('Failure condition triggered') 
            with session.begin():
                new_employee = Employee(name = employee_data['name'], position = employee_data['position'])
                session.add(new_employee)
                session.commit()
            session.refresh(new_employee)      #what does refresh do
            return new_employee
       
       except Exception as e:
           return e

def find_all():
    query = select(Employee)              #why doesn't this one need "with session"
    employees = db.session.execute(query).scalars().all()
    return employees
