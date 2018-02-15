# import tools to use operating system functionality
import os
# import functions and variables to manipulate runtime env
import sys
# import functions for writing mapper
from sqlalchemy import Column, ForeignKey, Integer, String
# import functions for config and class
from sqlalchemy.ext.declarative import declarative_base
# import functions to create foreign key relationships in mapper
from sqlalchemy.orm import relationship
# import class necessary for generating engine
from sqlalchemy import create_engine
Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
        }


class MenuItem(Base):
    __tablename__ = 'menu_item'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    @property
    def serialize(self):
        # returns data in easily serializeable JSON format
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }


# insert at end of file
# create an instance of create_engine class
# create a new db file that be used similarly to robust db systems
engine = create_engine('postgresql://evans:evans123@localhost:5432/rest')

# connect to db, add created classes to db as tables
Base.metadata.create_all(engine)
