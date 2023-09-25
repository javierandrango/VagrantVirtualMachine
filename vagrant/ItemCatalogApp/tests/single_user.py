# append directory
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
flask_app_path = os.path.join(current_dir, '..', 'flask_app')
sys.path.append(flask_app_path)

# ORM modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DB setup module
from db_setup import Base, User


# DB configuration
engine = create_engine('sqlite:///../catalogDBSetup.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

user1 = User(
    username='javier',
    email='fjxvierxnd@gmail.com',
    picture='https://lh3.googleusercontent.com/a/ACg8ocLScXKOI_kQsGdSFRaAsH50izDTUuhTfHyaJRWd1zqd7Q=s432-c-no'
)
user1.hash_password('javier')
session.add(user1)
session.commit()