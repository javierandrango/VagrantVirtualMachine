from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'
    name = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)

    # share information in json format
    @property
    def serialize(self):
        # return object data in easily serializable format:
        return{
            'name': self.name,
            'id': self.id
        }


class MenuItem(Base):
    __tablename__ = 'menuitem'
    name = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    # share information in json format
    @property
    def serialize(self):
        # return object data in easily serializable format:
        return{
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
