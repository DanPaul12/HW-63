from models.models import User
from sqlalchemy.orm import Session
from models.models import db
from models.schemas import users_schema
from sqlalchemy import select

def save(user_data):
    with Session(db.engine) as session:
        with session.begin():
            new_user = User(username=user_data['username'], password=user_data['password'], role=user_data['role'])
            session.add(new_user)
            session.commit()
        session.refresh(new_user)
        return new_user
    
def find_all():
    query = select(User)
    users = db.session.execute(query).scalars().all()
    return users