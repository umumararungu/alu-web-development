#!/usr/bin/env python3
"""User Authentication"""

import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    reset_token = Column(String, nullable=True)

    def __repr__(self):
       return "<User(email='%s', session_id='%s', hashed_password='%s')>" % (
                            self.email, self.hashed_password, self.session_id)
