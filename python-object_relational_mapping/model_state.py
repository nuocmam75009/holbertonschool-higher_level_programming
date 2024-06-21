#!/usr/bin/python3
"""
        Implement a class State that inherits from Base
        linked to 'states' table of MySQL server
        MySQL server running on localhost port 3306
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(
        Integer,
            primary_key=True,
            autoincrement=True,
            nullable=False
        )
    name = Column(
        String(128),
        nullable=False
        )

engine = create_engine('mysql://root:lucaslucas@localhost:3306/hbtn_0e_6_usa', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
