# DB modules
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# hashing password
from passlib.apps import custom_app_context as pwd_context

# token authentication modules
from itsdangerous import URLSafeTimedSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
import random, string

# data base migration modules 
from alembic import context

# create DB base
Base = declarative_base()

# generate a random secret key of lenght 32
secret_key = ''.join(random.choice(string.ascii_uppercase+string.digits) for _ in range(32))

# DB tables
# user table
class User (Base):
    __tablename__ = 'user'
    id= Column(Integer, primary_key=True)    
    username= Column(String(32), index = True)
    email= Column(String(320))
    picture= Column(String) 
    password_hash= Column(String(64))
    password_salt= Column(String(64))

    # store hash from a password
    #def hash_password(self, password):
    #    self.password_hash = pwd_context.hash(password)
    
    # verify password
    #def verify_password(self,password):
    #    return pwd_context.verify(password,self.password_hash)
    
    # encoded auth token
    def generate_auth_token(self):
        s = Serializer(secret_key)
        return s.dumps({'id':self.id})

    # verify valid token
    @staticmethod
    def verify_auth_token(token):
        s = Serializer(secret_key)
        try:
            data = s.loads(token,max_age=600)
        except SignatureExpired:
            # valid token but expired
            return None
        except BadSignature:
            # invalid token
            return None
        user_id = data['id']
        return user_id

class Categories(Base):
    __tablename__='category'
    id = Column(Integer, primary_key=True) 
    user_id = Column(Integer, ForeignKey('user.id'))
    name = Column(String(64), nullable=False)
    user = relationship(User)
    
    # share information in json format
    @property
    def serialize(self):
        return{
            'id':self.id,
            'name':self.name,
        }

class ItemCategory(Base):
    __tablename__='itemcategory'
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    item = Column(String(64), nullable=False)
    description = Column(String, nullable=False)
    user = relationship(User)
    category = relationship(Categories)

    # share information in json format
    @property
    def serialize(self):
        return{
            'category id':self.category_id,
            'item id':self.id,
            'item':self.item,
            'description':self.description,
        }


engine = create_engine('sqlite:///../catalogDBSetup.db')
Base.metadata.create_all(engine) 

'''
if __name__ == '__main__':
    #add new item-colum in User Table
    with engine.connect() as conn:
        conn.execute("INSERT INTO user (password_salt) VALUES ('1234')")
'''    