# DB modules
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# hashing password
from passlib.apps import custom_app_context as pwd_context

# token authentication modules
from itsdangerous import URLSafeTimedSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
import random, string

# create DB base
Base = declarative_base()

# generate a random secret key of lenght 32
secret_key = ''.join(random.choice(string.ascii_uppercase+string.digits) for _ in range(32))


# DB tables
class User (Base):
    __tablename__ = 'user'
    id= Column(Integer, primary_key=True)    
    username= Column(String(32), index = True)
    email= Column(String(320))
    picture= Column(String)
    password_hash= Column(String(64))

    # store hash from a password
    def hash_password(self, password):
        self.password_hash = pwd_context.hash(password)
    
    # verify password
    def verify_password(self,password):
        return pwd_context.verify(password,self.password_hash)
    
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

engine = create_engine('sqlite:///catalogDBSetup.db')
Base.metadata.create_all(engine) 
