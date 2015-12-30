import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Catagory(Base):
    __tablename__ = 'catagory'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):

        return {
            'name': self.name,
            'id': self.id,
        }


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    description = Column(String, nullable = False)
    image = Column(String)
    catagory_id = Column(Integer, ForeignKey('catagory.id'))
    catagory = relationship(Catagory, single_parent=True ,cascade="all, delete-orphan")

    @property
    def serialize(self):

        return {
        	'cat_id' : self.catagory_id,
            'description': self.description,
            'title': self.title,
            'id': self.id
        }

engine = create_engine('sqlite:///itemscatalog.db')


Base.metadata.create_all(engine)