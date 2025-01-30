#!/usr/bin/env python3
""""hashed password"""


import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from db import DB
from user import User


def _hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ return a string representation of a new UUID """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """initial function"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """registering user function"""
        try:
            _user = self._db.find_user_by(email=email)
        except NoResultFound:
            _password = _hash_password(password)
            _user = self._db.add_user(email, _password)
            return _user
        else:
            raise ValueError('User{email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """login validation function"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        else:
            return bcrypt.checkpw(password=password.encode('utf-8'),
                                  hashed_password=user.hashed_password)
