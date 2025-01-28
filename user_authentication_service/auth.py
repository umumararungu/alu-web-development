#!/usr/bin/env python3
""""hashed passorword"""


import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from db import DB
from user import User


def _hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('útf-8'), bcrypt.gensalt())
