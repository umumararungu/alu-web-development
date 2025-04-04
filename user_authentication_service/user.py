#!/usr/bin/env python3
"""User Authentication"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)


class User(Base):
    """User class"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    hashed_password = Column(String(250), nullable=False)
    reset_token = Column(String(250), nullable=True)
