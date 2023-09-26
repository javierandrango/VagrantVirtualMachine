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


# user created with the first database configuration
user_exist = session.query(User).filter_by(id=1).one()
if (not user_exist):
    user1 = User(
        username='javier',
        email='fjxvierxnd@gmail.com',
        picture='https://lh3.googleusercontent.com/a/ACg8ocLScXKOI_kQsGdSFRaAsH50izDTUuhTfHyaJRWd1zqd7Q=s432-c-no'
    )
    user1.hash_password('javier')
    session.add(user1)
    session.commit()
    print('first user added successfully')
else:
    print('first user already exist')


# user created after the first migration (database 'user' table updated)
# the hashing process was moved to frontend 
update_user = session.query(User).filter_by(id=1).one()
update_user.password_salt = "$2a$10$e/kHhQ3bNuDono.BlbSb/."
update_user.password_hash = "$2a$10$e/kHhQ3bNuDono.BlbSb/.I95SnVD69PkfOIQbvrg58DTS.InHBem"
session.add(update_user)
session.commit()
print("first user updated successfully")