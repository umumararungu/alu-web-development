#!/usr/bin/env python3
"""database creation"""


from requests import session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from user import Base, User
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

# engine = create_engine("mysql://scott:tiger@hostname/dbname",
#                             encoding='latin1', echo=True)
Session = sessionmaker()


class DB:

    def __init__(self):
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        adding_user = User(email=email, hashed_password=hashed_password)
        self._session.add(adding_user)
        self._session.commit()
        return adding_user

    def find_user_by(self, **kwargs) -> User:
        if kwargs is None:
            raise InvalidRequestError
        finder = self._session.query(User).filter_by(**kwargs).first()

        if finder is None:
            raise NoResultFound

        return finder

    def update_user(self, user_id: int, **kwargs) ->  None:
        id_to_update = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(id_to_update, key):
                raise ValueError
            setattr(id_to_update, key, value)
        self._session.commit()
