from sqlalchemy import Colum, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'
    name = Colum(String(250), nullable=False)
    id = Colum(Integer, primary_key=True)


class MenuItem(Base):
    __tablename__ = 'menuitem'
    name = Colum(String(250), nullable=False)
    id = Colum(Integer, primary_key=True)
    course = Colum(String(250))
    description = Colum(String(250))
    price = Colum(String(250))
    restaurant_id = Colum(Integer, nullable=False)
    restaurant = relationship(Restaurant)


engine = create_engine('sqlite:///restaurant.db')
Base.metadata.create_all(engine)
